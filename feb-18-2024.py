# Good morning! Here's your coding interview problem for today.
# This problem was asked by Dropbox.
# Implement an efficient string matching algorithm.
# That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
# If the pattern is found, return the start index of its location. If not, return False.

from collections import deque
class LRU:
    def __init__(self, size):
        self.size = size
        self.current_keys = deque()
        self.cache = {}
    
    def set(self, key, value):
        if len(self.current_keys) == self.size:
            del self.cache[self.current_keys[-1]] 
            self.current_keys.pop()
        self.current_keys.appendleft(key)
        self.cache[key] = value
    
    def get(self, key):
        if key in self.cache:
            return self.cache[key]

        return "Not Found"

obj1 = LRU(2)
obj1.set('pos1', 12)
obj1.set('pos2', 13)
obj1.set('pos3', 14)
print(obj1.get('pos2'))



