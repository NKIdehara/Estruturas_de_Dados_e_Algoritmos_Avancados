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

    def find(self, prefix):
        def _find_node(node, prefix): # encontrar começo do nó
            for char in prefix:
                if char not in node.children:
                    return None
                node = node.children[char]
            return node

        def _collect_nodes(node, current_word, words): # junta os caracteres da palavra
            if node.is_end_of_word:
                words.append(current_word) # palavra completa
            for char, child in node.children.items():
                _collect_nodes(child, current_word + char, words)

        words = []
        node = _find_node(self.root, prefix)
        if node:
            _collect_nodes(node, prefix, words)
        return words

lista = ["casa", "carro", "caminhão", "cachorro", "cadeira", "chocolate"]
trie = Trie()
for i in lista:
    trie.insert(i)
palavra = "chocolate"
print(f"{palavra} está em Trie: {trie.search(palavra)}")
trie.print_trie()

prefixo = "ca"
print(f"todas as palavras com o prefixo {prefixo}: {trie.find(prefixo)}")