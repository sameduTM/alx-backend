#!/usr/bin/python3
""" Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    """

    def __init__(self) -> None:
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add item to cache with given key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get item given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
