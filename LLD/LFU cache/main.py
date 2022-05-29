import collections
class Node:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None
        
class DLL:
    def __init__(self):
        self._size = 0
        self.head = Node()
        self.head.next = self.head.prev = self.head
    
    def __len__(self):
        return self._size
    
    def append(self,node):
        
        node.next=self.head.next
        node.prev = self.head
        
        self.head.next = node
        node.next.prev = node
        
        self._size+=1
    
    def pop(self,node=None):
        
        if self._size==0:
            return
        if not node:
            node = self.head.prev
        
        node.next.prev = node.prev
        node.prev.next = node.next
        
        self._size-=1
        
        return node
        
        
        
class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.size = 0
        
        self.lookup = {}
        self.freq_lookup = collections.defaultdict(DLL)
        self.min_freq = 0
      
    def _update(self,node):
        
        frq = node.freq
        self.freq_lookup[frq].pop(node)
        node.freq +=1
        if frq==self.min_freq and not len(self.freq_lookup[frq]):
            self.min_freq+=1
        
        self.freq_lookup[node.freq].append(node)
        
        
        

    def get(self, key: int):
        if key not in self.lookup:
            return -1
        node = self.lookup.get(key)
        self._update(node)
        return node.val

        

    def put(self, key: int, value: int):
        if key in self.lookup:
            node = self.lookup.get(key)
            node.val = value
            self._update(node)
        else:
            if self.size==self.capacity:
                popped = self.freq_lookup[self.min_freq].pop()
                del self.lookup[popped.key]
                self.size-=1
            
            node = Node(key,value)
            self.lookup[key] = node
            self.min_freq = 1
            self.freq_lookup[1].append(node)
            self.size+=1
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lfu = LFUCache(2);
lfu.put(1, 1);   # cache=[1,_], cnt(1)=1
lfu.put(2, 2);   # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      # return 1
                 # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 # cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      # return -1 (not found)
lfu.get(3);      # return 3
                 # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 # cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      # return -1 (not found)
lfu.get(3);      # return 3
                 # cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      # return 4
                 # cache=[4,3], cnt(4)=2, cnt(3)=3
                 
                 
print([(x.key,x.val,x.freq) for x in lfu.lookup.values()])