#!/usr/bin/python3
""" LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
    """
    n_list = []

    def __init__(self) -> None:
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item) -> None:
        """ Assign to cache item with key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.n_list.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(self.n_list[-2])
            print(f"DISCARD: {self.n_list[-2]}")

    def get(self, key):
        """ Get item given key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
