from tkinter.messagebox import NO


class ListNode:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
    
        