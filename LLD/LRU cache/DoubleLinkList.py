from ListNode import ListNode
class DoubleLinkList:
    
    def __init__(self):
        
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.previous = self.head

    def set_links_to_front(self,node):
        # node links
        node.next = self.head.next
        node.previous = self.head
        # neighbour links
        self.head.next = node
        node.next.previous = node
    
    def delete_links_of_node(self,node):
        # set links of neighbour
        prev = node.previous
        next = node.next
        
        prev.next = next
        next.previous = prev
        
    def add_to_front(self,key,val):
        node = ListNode(key,val)
        self.set_links_to_front(node)
        return node
        
    def move_to_front(self,node):
        self.delete_links_of_node(node)
        self.set_links_to_front(node)
        
    def delete_from_tail(self):
        if self.tail.previous == self.head:
            return None
        node = self.tail.previous
        self.delete_links_of_node(node)
        return node
        
        