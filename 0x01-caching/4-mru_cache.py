#!/usr/bin/python3
""" MRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item assigned to a key
        """
        if key is None or item is None:
            return
        keys_list = list(self.cache_data)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        if len(self.cache_data) >= self.MAX_ITEMS:
            self.cache_data.popitem(last=True)
            print(f"DISCARD: {keys_list[-1]}")
        self.cache_data[key] = item

    def get(self, key):
        """ Get item given key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
