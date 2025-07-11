#!/usr/bin/python3
""" FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class
    """

    def __init__(self) -> None:
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add item to cache at given key
        """
        if key is None or item is None:
            return None
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_list = list(self.cache_data)
            print(f"DISCARD: {key_list[0]}")
            self.cache_data.pop(0)
        self.cache_data[key] = item

    def get(self, key):
        """ Get item given key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data
        return None
