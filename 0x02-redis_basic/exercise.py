#!/usr/bin/python3
"""Create a Cache class
__init__ method, store an instance of the Redis client as a private variable named
"""
import uuid
import redis
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

