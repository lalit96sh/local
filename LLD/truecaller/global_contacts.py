from commons.contact_trie import ContactTrie

class GlobalContacts:
    def __init__(self):
        self.global_contact_trie = ContactTrie()
        self.spam_contact_trie = set()