class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        if len(self.children) == 0:
            return results

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        for char in self.children:
            results.extend(self.children[char].suffixes(suffix=suffix+char))

        return results
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return node

############################### Test #################################
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

result1 = MyTrie.find('tri')
print(result1)
result2 = result1.suffixes()
print(result2)  # return ['e', 'gger', 'gonometry', 'pod']

result1 = MyTrie.find('an')
print(result1)
result2 = result1.suffixes()
print(result2)  # return ['t', 'thology', 'tagonist', 'tonym']

result1 = MyTrie.find('')
print(result1)
result2 = result1.suffixes()
print(result2)  # return ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
