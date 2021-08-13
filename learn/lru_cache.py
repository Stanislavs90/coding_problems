from typing import List

"""
Left - least recently used used


Right - most recent


"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} #map key to node

        self.left = Node(0,0)
        self.right = Node(0,0)

        # Left = least recently used
        self.left.next = self.right
        # right= most recent
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev 


    # insert node at right 
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right 

        prev.next = node
        nxt.prev = node 

        node.next = nxt
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from the hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
#LRUCache lRUCache = new LRUCache(2);
lRUCache = LRUCache(2)
lRUCache.put(1, 1); #// cache is {1=1}
lRUCache.put(2, 2); #// cache is {1=1, 2=2}
lRUCache.get(1);    #// return 1
lRUCache.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    #// returns -1 (not found)
lRUCache.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    #// return -1 (not found)
lRUCache.get(3);    #// return 3
lRUCache.get(4);    #// return 4