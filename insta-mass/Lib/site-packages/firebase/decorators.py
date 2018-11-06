import requests
from functools import wraps


def http_connection(timeout):
    """
    Decorator function that injects a requests.Session instance into
    the decorated function's actual parameters if not given.
    """
    def wrapper(f):
        def wrapped(*args, **kwargs):
            if not ('connection' in kwargs) or not kwargs['connection']:
                connection = requests.Session()
                kwargs['connection'] = connection
            else:
                connection = kwargs['connection']
            connection.timeout = timeout
            connection.headers.update({'Content-type': 'application/json'})
            return f(*args, **kwargs)
        return wraps(f)(wrapped)
    return wrapper
