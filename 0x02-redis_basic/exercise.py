#!/usr/bin/python3
"""Create a Cache class
__init__ method, store an instance of the Redis client as a private variable named
"""
import uuid
import redis
from typing import Callable, Optional, Union
r = redis.Redis(host='localhost', port=6379, db=0)


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, str, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda x: int(x))
    def call_history(method: Callable) -> Callable:
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"
            r.rpush(inputs_key, str(args))
            result = method(*args, **kwargs)
            r.rpush(outputs_key, str(result))
            return result
        return wrapperclass Cache:
   class Cache:
    @call_history
    def store(self, key: str, value: str, timeout: int = None):
        self.client.set(key, value, ex=timeout)


    

