#!/usr/bin/env python3
"""doc doc"""
import redis
import uuid
from typing import Union


class Cache:
    """doc doc"""

    def __init__(self):
        """doc doc"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
