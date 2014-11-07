class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        #import collections
        self.capacity = capacity
        self.data = collections.OrderedDict()


    # @return an integer
    def get(self, key):
        if  not key in self.data:
            return -1
        value = self.data.pop(key)
        self.data[key] = value
        return value
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.data:
            self.data.pop(key)
        elif len(self.data) == self.capacity:
            self.data.popitem(last=False)
        self.data[key] = value
            
            
            