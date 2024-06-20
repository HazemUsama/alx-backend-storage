#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from funtools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count requests"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        r.incr(f"count:{url}")
        result = r.get(url)
        if result:
            return result.decode('utf-8')
        result = method(url) r.setex(url, 10, result)
        return result
    return wrapper


def get_page(url: str) -> str:
    """Get page"""
    result = requests.get(url).text
    return result
