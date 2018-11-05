import multiprocessing

from .lazy import LazyLoadProxy

__all__ = ['process_pool']

_process_pool = None
def get_process_pool(size=5):
    global _process_pool
    if _process_pool is None:
        _process_pool = multiprocessing.Pool(processes=size)
    return _process_pool
process_pool = LazyLoadProxy(get_process_pool)

