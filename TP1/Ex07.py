class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children: # caracter atual não faz parte da palavra
                return False
            node = node.children[char]
        return node.is_end_of_word # encontrou palavra completa

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root
        if node.is_end_of_word: # palavra completa
            print(f"Palavra: {prefix}")
        for char, child in node.children.items():
            self.print_trie(child, prefix + char) # junta caracteres de forma recursiva

lista = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
trie = Trie()
for i in lista:
    trie.insert(i)
print(trie.search("casa"))
trie.print_trie()