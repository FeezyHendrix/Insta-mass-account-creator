try:
    import urlparse
except ImportError:
    #py3k
    from urllib import parse as urlparse

import json

from .firebase_token_generator import FirebaseTokenGenerator
from .decorators import http_connection

from .async import process_pool
from .jsonutil import JSONEncoder

__all__ = ['FirebaseAuthentication', 'FirebaseApplication']


@http_connection(60)
def make_get_request(url, params, headers, connection):
    """
    Helper function that makes an HTTP GET request to the given firebase
    endpoint. Timeout is 60 seconds.
    `url`: The full URL of the firebase endpoint (DSN appended.)
    `params`: Python dict that is appended to the URL like a querystring.
    `headers`: Python dict. HTTP request headers.
    `connection`: Predefined HTTP connection instance. If not given, it
    is supplied by the `decorators.http_connection` function.

    The returning value is a Python dict deserialized by the JSON decoder. However,
    if the status code is not 2x or 403, an requests.HTTPError is raised.

    connection = connection_pool.get_available_connection()
    response = make_get_request('http://firebase.localhost/users', {'print': silent'},
                                {'X_FIREBASE_SOMETHING': 'Hi'}, connection)
    response => {'1': 'John Doe', '2': 'Jane Doe'}
    """
    timeout = getattr(connection, 'timeout')
    response = connection.get(url, params=params, headers=headers, timeout=timeout)
    if response.ok or response.status_code == 403:
        return response.json() if response.content else None
    else:
        response.raise_for_status()


@http_connection(60)
def make_put_request(url, data, params, headers, connection):
    """
    Helper function that makes an HTTP PUT request to the given firebase
    endpoint. Timeout is 60 seconds.
    `url`: The full URL of the firebase endpoint (DSN appended.)
    `data`: JSON serializable dict that will be stored in the remote storage.
    `params`: Python dict that is appended to the URL like a querystring.
    `headers`: Python dict. HTTP request headers.
    `connection`: Predefined HTTP connection instance. If not given, it
    is supplied by the `decorators.http_connection` function.

    The returning value is a Python dict deserialized by the JSON decoder. However,
    if the status code is not 2x or 403, an requests.HTTPError is raised.

    connection = connection_pool.get_available_connection()
    response = make_put_request('http://firebase.localhost/users',
                                '{"1": "Ozgur Vatansever"}',
                                {'X_FIREBASE_SOMETHING': 'Hi'}, connection)
    response => {'1': 'Ozgur Vatansever'} or {'error': 'Permission denied.'}
    """
    timeout = getattr(connection, 'timeout')
    response = connection.put(url, data=data, params=params, headers=headers,
                              timeout=timeout)
    if response.ok or response.status_code == 403:
        return response.json() if response.content else None
    else:
        response.raise_for_status()


@http_connection(60)
def make_post_request(url, data, params, headers, connection):
    """
    Helper function that makes an HTTP POST request to the given firebase
    endpoint. Timeout is 60 seconds.
    `url`: The full URL of the firebase endpoint (DSN appended.)
    `data`: JSON serializable dict that will be stored in the remote storage.
    `params`: Python dict that is appended to the URL like a querystring.
    `headers`: Python dict. HTTP request headers.
    `connection`: Predefined HTTP connection instance. If not given, it
    is supplied by the `decorators.http_connection` function.

    The returning value is a Python dict deserialized by the JSON decoder. However,
    if the status code is not 2x or 403, an requests.HTTPError is raised.

    connection = connection_pool.get_available_connection()
    response = make_put_request('http://firebase.localhost/users/',
       '{"Ozgur Vatansever"}', {'X_FIREBASE_SOMETHING': 'Hi'}, connection)
    response => {u'name': u'-Inw6zol_2f5ThHwVcSe'} or {'error': 'Permission denied.'}
    """
    timeout = getattr(connection, 'timeout')
    response = connection.post(url, data=data, params=params, headers=headers,
                               timeout=timeout)
    if response.ok or response.status_code == 403:
        return response.json() if response.content else None
    else:
        response.raise_for_status()


@http_connection(60)
def make_patch_request(url, data, params, headers, connection):
    """
    Helper function that makes an HTTP PATCH request to the given firebase
    endpoint. Timeout is 60 seconds.
    `url`: The full URL of the firebase endpoint (DSN appended.)
    `data`: JSON serializable dict that will be stored in the remote storage.
    `params`: Python dict that is appended to the URL like a querystring.
    `headers`: Python dict. HTTP request headers.
    `connection`: Predefined HTTP connection instance. If not given, it
    is supplied by the `decorators.http_connection` function.

    The returning value is a Python dict deserialized by the JSON decoder. However,
    if the status code is not 2x or 403, an requests.HTTPError is raised.

    connection = connection_pool.get_available_connection()
    response = make_put_request('http://firebase.localhost/users/1',
       '{"Ozgur Vatansever"}', {'X_FIREBASE_SOMETHING': 'Hi'}, connection)
    response => {'Ozgur Vatansever'} or {'error': 'Permission denied.'}
    """
    timeout = getattr(connection, 'timeout')
    response = connection.patch(url, data=data, params=params, headers=headers,
                                timeout=timeout)
    if response.ok or response.status_code == 403:
        return response.json() if response.content else None
    else:
        response.raise_for_status()


@http_connection(60)
def make_delete_request(url, params, headers, connection):
    """
    Helper function that makes an HTTP DELETE request to the given firebase
    endpoint. Timeout is 60 seconds.
    `url`: The full URL of the firebase endpoint (DSN appended.)
    `params`: Python dict that is appended to the URL like a querystring.
    `headers`: Python dict. HTTP request headers.
    `connection`: Predefined HTTP connection instance. If not given, it
    is supplied by the `decorators.http_connection` function.

    The returning value is NULL. However, if the status code is not 2x or 403,
    an requests.HTTPError is raised.

    connection = connection_pool.get_available_connection()
    response = make_put_request('http://firebase.localhost/users/1',
                                {'X_FIREBASE_SOMETHING': 'Hi'}, connection)
    response => NULL or {'error': 'Permission denied.'}
    """
    timeout = getattr(connection, 'timeout')
    response = connection.delete(url, params=params, headers=headers, timeout=timeout)
    if response.ok or response.status_code == 403:
        return response.json() if response.content else None
    else:
        response.raise_for_status()


class FirebaseUser(object):
    """
    Class that wraps the credentials of the authenticated user. Think of
    this as a container that holds authentication related data.
    """
    def __init__(self, email, firebase_auth_token, provider, id=None):
        self.email = email
        self.firebase_auth_token = firebase_auth_token
        self.provider = provider
        self.id = id


class FirebaseAuthentication(object):
    """
    Class that wraps the Firebase SimpleLogin mechanism. Actually this
    class does not trigger a connection, simply fakes the auth action.

    In addition, the provided email and password information is totally
    useless and they never appear in the ``auth`` variable at the server.
    """
    def __init__(self, secret, email, debug=False, admin=False, extra=None):
        self.authenticator = FirebaseTokenGenerator(secret, debug, admin)
        self.email = email
        self.provider = 'password'
        self.extra = (extra or {}).copy()
        self.extra.update({'debug': debug, 'admin': admin,
                           'email': self.email, 'provider': self.provider})

    def get_user(self):
        """
        Method that gets the authenticated user. The returning user has
        the token, email and the provider data.
        """
        token = self.authenticator.create_token(self.extra)
        user_id = self.extra.get('id')
        return FirebaseUser(self.email, token, self.provider, user_id)


class FirebaseApplication(object):
    """
    Class that actually connects with the Firebase backend via HTTP calls.
    It fully implements the RESTful specifications defined by Firebase. Data
    is transmitted as in JSON format in both ways. This class needs a DSN value
    that defines the base URL of the backend, and if needed, authentication
    credentials are accepted and then are taken into consideration while
    constructing HTTP requests.

    There are also the corresponding asynchronous versions of each HTTP method.
    The async calls make use of the on-demand process pool defined under the
    module `async`.

    auth = FirebaseAuthentication(FIREBASE_SECRET, 'firebase@firebase.com', 'fbpw')
    firebase = FirebaseApplication('https://firebase.localhost', auth)

    That's all there is. Then you start connecting with the backend:

    json_dict = firebase.get('/users', '1', {'print': 'pretty'})
    print json_dict
    {'1': 'John Doe', '2': 'Jane Doe', ...}

    Async version is:
    firebase.get('/users', '1', {'print': 'pretty'}, callback=log_json_dict)

    The callback method is fed with the returning response.
    """
    NAME_EXTENSION = '.json'
    URL_SEPERATOR = '/'

    def __init__(self, dsn, authentication=None):
        assert dsn.startswith('https://'), 'DSN must be a secure URL'
        self.dsn = dsn
        self.authentication = authentication

    def _build_endpoint_url(self, url, name=None):
        """
        Method that constructs a full url with the given url and the
        snapshot name.

        Example:
        full_url = _build_endpoint_url('/users', '1')
        full_url => 'http://firebase.localhost/users/1.json'
        """
        if not url.endswith(self.URL_SEPERATOR):
            url = url + self.URL_SEPERATOR
        if name is None:
            name = ''
        return '%s%s%s' % (urlparse.urljoin(self.dsn, url), name,
                           self.NAME_EXTENSION)

    def _authenticate(self, params, headers):
        """
        Method that simply adjusts authentication credentials for the
        request.
        `params` is the querystring of the request.
        `headers` is the header of the request.

        If auth instance is not provided to this class, this method simply
        returns without doing anything.
        """
        if self.authentication:
            user = self.authentication.get_user()
            params.update({'auth': user.firebase_auth_token})
            headers.update(self.authentication.authenticator.HEADERS)

    @http_connection(60)
    def get(self, url, name, connection, params=None, headers=None):
        """
        Synchronous GET request.
        """
        if name is None: name = ''
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        return make_get_request(endpoint, params, headers, connection=connection)

    def get_async(self, url, name, callback=None, params=None, headers=None):
        """
        Asynchronous GET request with the process pool.
        """
        if name is None: name = ''
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        process_pool.apply_async(make_get_request,
            args=(endpoint, params, headers), callback=callback)

    @http_connection(60)
    def put(self, url, name, data, connection, params=None, headers=None):
        """
        Synchronous PUT request. There will be no returning output from
        the server, because the request will be made with ``silent``
        parameter. ``data`` must be a JSONable value.
        """
        assert name, 'Snapshot name must be specified'
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        return make_put_request(endpoint, data, params, headers,
                                connection=connection)

    def put_async(self, url, name, data, callback=None, params=None, headers=None):
        """
        Asynchronous PUT request with the process pool.
        """
        if name is None: name = ''
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        process_pool.apply_async(make_put_request,
                                 args=(endpoint, data, params, headers),
                                 callback=callback)

    @http_connection(60)
    def post(self, url, data, connection, params=None, headers=None):
        """
        Synchronous POST request. ``data`` must be a JSONable value.
        """
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, None)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        return make_post_request(endpoint, data, params, headers,
                                 connection=connection)

    def post_async(self, url, data, callback=None, params=None, headers=None):
        """
        Asynchronous POST request with the process pool.
        """
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, None)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        process_pool.apply_async(make_post_request,
                                 args=(endpoint, data, params, headers),
                                 callback=callback)

    @http_connection(60)
    def patch(self, url, data, connection, params=None, headers=None):
        """
        Synchronous POST request. ``data`` must be a JSONable value.
        """
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, None)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        return make_patch_request(endpoint, data, params, headers,
                                  connection=connection)

    def patch_async(self, url, data, callback=None, params=None, headers=None):
        """
        Asynchronous PATCH request with the process pool.
        """
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, None)
        self._authenticate(params, headers)
        data = json.dumps(data, cls=JSONEncoder)
        process_pool.apply_async(make_patch_request,
                                 args=(endpoint, data, params, headers),
                                 callback=callback)

    @http_connection(60)
    def delete(self, url, name, connection, params=None, headers=None):
        """
        Synchronous DELETE request. ``data`` must be a JSONable value.
        """
        if not name: name = ''
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        return make_delete_request(endpoint, params, headers, connection=connection)

    def delete_async(self, url, name, callback=None, params=None, headers=None):
        """
        Asynchronous DELETE request with the process pool.
        """
        if not name: name = ''
        params = params or {}
        headers = headers or {}
        endpoint = self._build_endpoint_url(url, name)
        self._authenticate(params, headers)
        process_pool.apply_async(make_delete_request,
                    args=(endpoint, params, headers), callback=callback)
