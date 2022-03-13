from DoubleLinkList import DoubleLinkList
DEFAULT_CACHE_SIZE=5
class LRUCache:
    
    def __init__(self,capacity=DEFAULT_CACHE_SIZE):
        self.lookup = {}
        self.double_link_list=DoubleLinkList()
        self.size = 0
        self.max_size = capacity
    
    def get(self,key):
        if key in self.lookup:
            node = self.lookup.get(key)
            self.double_link_list.move_to_front(node)
            return node.value
        return None
    def set(self,key,value):
        if key in self.lookup:
            node = self.lookup.get(key)
            node.value = value
            self.double_link_list.move_to_front(node)
        else:
            self.size+=1
            node = self.double_link_list.add_to_front(key,value)
            self.lookup[key] = node
        
        if self.size>self.max_size:
            node = self.double_link_list.delete_from_tail()
            del self.lookup[node.key]
            self.size = self.max_size
    def print_cache(self):
        print("{")
        for key in self.lookup:
            print("\t{} : {} ".format(key,self.lookup[key].value))
        print("}")
                
            
        

