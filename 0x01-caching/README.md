# 0x01. Caching

## Description

In this project, you will learn about different caching algorithms and implement them in Python. Caching is a technique used to store frequently accessed data in a temporary storage area to improve performance. You will implement various caching strategies such as FIFO, LIFO, LRU, MRU, and LFU.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of Google:

- What a caching system is
- What FIFO (First In First Out) means
- What LIFO (Last In First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- The purpose of a caching system
- The limitations of a caching system

## Resources

Read or watch:

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_(LFU))

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation

## Parent Class: BaseCaching

All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
