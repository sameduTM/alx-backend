#!/usr/bin/python3
""" LFU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.freq_items = defaultdict(OrderedDict)

    def _evict_lfu(self):
        """ Evict the least frequently used item """
        min_freq = min(self.freq_items)
        # Find the oldest item within that frequency
        evict_key, _ = self.freq_items[min_freq].popitem(last=False)
        # Remove from cache_data and frequency tracker
        del self.cache_data[evict_key]
        del self.frequency[evict_key]
        # Clean up empty frequency list
        if not self.freq_items[min_freq]:
            del self.freq_items[min_freq]
        return evict_key  # Return the evicted key

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and its frequency
            self.cache_data[key] = item
            self.get(key)  # To update its frequency
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                evict_key = self._evict_lfu()
                print(f"DISCARD: {evict_key}")
            # Add new item with frequency 1
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.freq_items[1][key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key not in self.cache_data:
            return None

        # Get current frequency and value
        freq = self.frequency[key]
        value = self.cache_data[key]

        # Remove from current frequency group
        self.freq_items[freq].pop(key)
        if not self.freq_items[freq]:
            del self.freq_items[freq]

        # Increment frequency and add to new frequency group
        self.frequency[key] += 1
        new_freq = self.frequency[key]
        self.freq_items[new_freq][key] = value

        return value
