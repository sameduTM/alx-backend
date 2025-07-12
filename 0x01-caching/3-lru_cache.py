#!/usr/bin/python3
""" LRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to cache with given key
        """
        if key is not None or item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            if key is None or item is None:
                return
            self.cache_data[key] = item
            keys_list = list(self.cache_data)
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.popitem(last=False)
                print(f"DISCARD: {keys_list[0]}")

    def get(self, key):
        """ Get item using given key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
