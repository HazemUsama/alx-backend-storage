#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable
from time import sleep



def count_requests(method: Callable) -> Callable:
    """Decorator to count requests"""
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        client = redis.Redis()
        client.incr(f"count:{url}")
        cached_html = client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        client.set(f"cached:{url}", html, 10)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get page"""
    result = requests.get(url).text
    return result
