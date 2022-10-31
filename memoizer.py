from typing import Callable
""" Memoizer decorator """

def memoized(func: Callable) -> Callable:
    input_hash_table = {}
    def inner(*args, **kwargs):
        input_hash = f"{args}; {kwargs}"
        if input_hash in input_hash_table:
            return input_hash_table[input_hash]
        result = func(*args, **kwargs)
        input_hash_table[input_hash] = result
        return result
    inner.__name__=func.__name__
    return inner
