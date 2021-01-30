

class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None 

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
    
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    
    def append(self, node):
        # self.tail.pre.next = self.node 
        # self.node.next = self.tail
        # self.node.pre = self.tail.pre
        # self.tail.pre = self.node
        
        node.pre, node.next = self.tail.pre, self.tail
        self.tail.pre.next = node
        self.tail.pre = node 


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.append(node)
            return self.dic[key].value

        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.append(node)
            self.dic[key].value = value
        else:
            if len(self.dic) >= self.capacity:
                node = self.head.next
                self.delete(node)
                del self.dic[node.key]

            new = Node(key, value)
            self.append(new)
            self.dic[key] = new



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
