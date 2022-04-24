
from global_contacts import GlobalContacts
from commons.contact_trie import ContactTrie
class User:
    def __init__(self,name=None,phone_number=None):
        self.phone_number = phone_number
        self.name = name
        self.blocked = set()
        self.contact_trie = ContactTrie() 
        
    def add_contact(self,contact):
        self.contact_trie.insert_into_trie(contact.name)
        self.contact_trie.insert_into_trie(contact.phone_number)
        
        
        