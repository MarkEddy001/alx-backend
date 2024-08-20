#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.last}")
                del self.cache_data[self.last]
            self.cache_data[key] = item
            self.last = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
