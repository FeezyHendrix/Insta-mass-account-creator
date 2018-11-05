##############################################################################
# THE ENTIRE CODE HAS BEEN TAKEN FROM THE OFFICIAL FIREBASE GITHUB           #
# REPOSITORY NAMED `firebase-token-generator-python` WITH SLIGHT             #
# MODIFICATIONS.                                                             #
#                                                                            #
# FOR MORE INFORMATION, PLEASE TAKE A LOOK AT THE ACTUAL REPOSITORY:         #
#  - https://github.com/firebase/firebase-token-generator-python             #
##############################################################################
import base64
import hashlib
import hmac
import json
import time

__all__ = ['FirebaseTokenGenerator']


class FirebaseTokenGenerator(object):
    TOKEN_VERSION = 0
    TOKEN_SEP = '.'
    CLAIMS_MAP = {
        'expires': 'exp',
        'notBefore': 'nbf',
        'admin': 'admin',
        'debug': 'debug',
        'simulate': 'simulate'
    }
    HEADERS = {'typ': 'JWT', 'alg': 'HS256'}

    def __init__(self, secret, debug=False, admin=False):
        assert secret, 'Your Firebase SECRET is not valid'
        self.secret = secret
        self.admin = admin
        self.debug = debug

    def create_token(self, data, options=None):
        """
        Generates a secure authentication token.

        Our token format follows the JSON Web Token (JWT) standard:
        header.claims.signature

        Where:
        1) 'header' is a stringified, base64-encoded JSON object containing version and algorithm information.
        2) 'claims' is a stringified, base64-encoded JSON object containing a set of claims:
            Library-generated claims:
            'iat' -> The issued at time in seconds since the epoch as a number
            'd' -> The arbitrary JSON object supplied by the user.
            User-supplied claims (these are all optional):
            'exp' (optional) -> The expiration time of this token, as a number of seconds since the epoch.
            'nbf' (optional) -> The 'not before' time before which the token should be rejected (seconds since the epoch)
            'admin' (optional) -> If set to true, this client will bypass all security rules (use this to authenticate servers)
            'debug' (optional) -> 'set to true to make this client receive debug information about security rule execution.
            'simulate' (optional, internal-only for now) -> Set to true to neuter all API operations (listens / puts
                       will run security rules but not actually write or return data).
        3) A signature that proves the validity of this token (see: http://tools.ietf.org/html/draft-ietf-jose-json-web-signature-07)

        For base64-encoding we use URL-safe base64 encoding. This ensures that the entire token is URL-safe
        and could, for instance, be placed as a query argument without any encoding (and this is what the JWT spec requires).

        Args:
            data - a json serializable object of data to be included in the token
            options - An optional dictionary of additional claims for the token. Possible keys include:
                a) 'expires' -- A timestamp (as a number of seconds since the epoch) denoting a time after which
                    this token should no longer be valid.
                b) 'notBefore' -- A timestamp (as a number of seconds since the epoch) denoting a time before
                    which this token should be rejected by the server.
                c) 'admin' -- Set to true to bypass all security rules (use this for your trusted servers).
                d) 'debug' -- Set to true to enable debug mode (so you can see the results of Rules API operations)
                e) 'simulate' -- (internal-only for now) Set to true to neuter all API operations (listens / puts
                                will run security rules but not actually write or return data)
        Returns:
            A signed Firebase Authentication Token
        Raises:
            ValueError: if an invalid key is specified in options
        """
        if not options:
            options = {}
        options.update({'admin': self.admin, 'debug': self.debug})
        claims = self._create_options_claims(options)
        claims['v'] = self.TOKEN_VERSION
        claims['iat'] = int(time.mktime(time.gmtime()))
        claims['d'] = data
        return self._encode_token(self.secret, claims)

    def _create_options_claims(self, opts):
        claims = {}
        for k in opts:
            if k in self.CLAIMS_MAP:
                claims[k] = opts[k]
            else:
                raise ValueError('Unrecognized Option: %s' % k)
        return claims

    def _encode(self, bytes):
        encoded = base64.urlsafe_b64encode(bytes)
        return encoded.decode('utf-8').replace('=', '')

    def _encode_json(self, obj):
        return self._encode(json.dumps(obj).encode("utf-8"))

    def _sign(self, secret, to_sign):
        def portable_bytes(s):
            try:
                return bytes(s, 'utf-8')
            except TypeError:
                return bytes(s)
        return self._encode(hmac.new(portable_bytes(secret), portable_bytes(to_sign),
                                     hashlib.sha256).digest())

    def _encode_token(self, secret, claims):
        encoded_header = self._encode_json(self.HEADERS)
        encoded_claims = self._encode_json(claims)
        secure_bits = '%s%s%s' % (encoded_header, self.TOKEN_SEP, encoded_claims)
        sig = self._sign(secret, secure_bits)
        return '%s%s%s' % (secure_bits, self.TOKEN_SEP, sig)
