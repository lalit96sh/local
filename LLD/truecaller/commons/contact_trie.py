from trie_node import TreiNode
from constants import WORD_END_CHAR
class ContactTrie:
    def __init__(self):
        self.root = TreiNode()
    
    def insert_into_trie(self,word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.children[WORD_END_CHAR] = TreiNode()
        
    def list_words_with_prefix(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                return []
            node = node.children[w]
        return self._get_words_startwith(node,word)
        
    def _get_words_startwith(self,node,word):
        
        wordlist = []
        
        def helper(node,prefix):
            if WORD_END_CHAR in node.children:
                wordlist.append(prefix)
            
            for key in node.children:
                if key!=WORD_END_CHAR:
                    helper(node.children[key],prefix+key)
        
        helper(node,word)
        return wordlist

        
    def remove_word_from_trie(self,word):
        node = self.root
        def dfs(node,word):
            if not word:
                if WORD_END_CHAR in node.children:
                    del node.children[WORD_END_CHAR]
                
                return node.children
            if word[0] in node.children:
                value = dfs(node.children[word[0]],word[1:])
                if not value:
                    del node.children[word[0]]
            
            return node.children
        
        dfs(node,word)
        
        
# cc = ContactTrie()
# cc.insert_into_trie("app")
# cc.insert_into_trie("apple")
# cc.insert_into_trie("application")
# cc.insert_into_trie("ape")

# print(cc.list_words_with_prefix("app"))
# print(cc.list_words_with_prefix("ap"))
# print(cc.list_words_with_prefix("xx"))


# cc.remove_word_from_trie("xy")
# cc.remove_word_from_trie("apple")
# cc.remove_word_from_trie("")

# print(cc.list_words_with_prefix("app"))
# print(cc.list_words_with_prefix("ap"))
# print(cc.list_words_with_prefix("xx"))






        
        