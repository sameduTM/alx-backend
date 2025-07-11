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
            return
        self.cache_data[key] = item
        keys_list = list(self.cache_data)
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(keys_list[0])
            print(f"DISCARD: {keys_list[0]}")

    def get(self, key):
        """ Get item given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
