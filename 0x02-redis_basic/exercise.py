#!/usr/bin/env python3
"""doc doc module"""

import redis
import uuid
from typing import Union


class Cache:
    """doc doc class"""

    def __init__(self):
        """doc doc method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """doc doc method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
