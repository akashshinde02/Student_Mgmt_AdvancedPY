"""Utility decorators for logging and timing"""
import time, functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"[TIME] {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

def require_auth(token_required="secret-token"):
    """Simulated auth decorator: checks kwargs for token"""
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = kwargs.get("token")
            if token != token_required:
                raise PermissionError("Invalid token")
            return func(*args, **kwargs)
        return wrapper
    return deco
