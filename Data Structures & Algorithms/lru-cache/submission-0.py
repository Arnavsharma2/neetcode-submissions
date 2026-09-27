class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int): 
        self.capacity = capacity 
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            temp = self.left.next 
            self.left.next = node
            node.next = temp
            node.prev = self.left
            temp.prev=node
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key] 
            node.value = value
            get(key)
        else:
            node = Node(key, value)
            self.cache[key] = node
            temp = self.left.next
            temp.prev = node
            node.next = temp
            self.left.next = node
            node.prev = self.left
        
        while len(self.cache) > self.capacity:
            scape = self.cache[self.right.prev.key]
            temp = scape.prev
            temp.next = self.right
            self.right.prev = temp
            del self.cache[scape.key]
        

        




        
