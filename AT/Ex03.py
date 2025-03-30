class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_nome = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no = self.raiz
        for caracter in palavra:
            if caracter not in no.filhos:
                no.filhos[caracter] = NoTrie()
            no = no.filhos[caracter]
        no.fim_nome = True

    def autocompletar(self, prefixo):
        no = self.raiz
        for caracter in prefixo:
            if caracter not in no.filhos:
                return [] # não existe sugestão
            no = no.filhos[caracter]
        sugestoes = []
        self._dfs(no, prefixo, sugestoes)
        return sugestoes

    def _dfs(self, no, prefixo, sugestoes): #sugestões encontradas: buscar todos
        if no.fim_nome:
            sugestoes.append(prefixo) # incluir sugestão encontrada
        for caracter, proximo_no in no.filhos.items():
            self._dfs(proximo_no, prefixo + caracter, sugestoes)

livros = [
    "Dom Quixote", "Um Conto de Duas Cidades", "O Senhor dos Anéis", "O Pequeno Príncipe",
    "Harry Potter e a Pedra Filosofal", "O Hobbit", "E não sobrou nenhum", "O Sonho da Câmara Vermelha",
    "Ela, a Feiticeira", "O Leão, a Feiticeira e o Guarda-Roupa", "O Código Da Vinci", "Pense e Enriqueça",
    "O Alquimista", "Harry Potter e o Enigma do Príncipe", "O Apanhador no Campo de Centeio", "Harry Potter e a Câmara Secreta",
    "Harry Potter e o Prisioneiro de Azkaban", "Harry Potter e o Cálice de Fogo", "Harry Potter e a Ordem da Fênix",
    "Harry Potter e as Relíquias da Morte", "Cem Anos de Solidão", "Lolita", "Heidi", "Meu Filho, Meu Tesouro", "Anne of Green Gables",
    "Beleza Negra", "O Nome da Rosa", "A Águia Pousou", "Era uma Vez em Watership Down", "O Relatório Hite sobre sexualidade feminina",
    "A Menina e o Porquinho", "Um Safado em Dublin", "As Pontes de Madison", "Ben-Hur: Uma História dos Tempos de Cristo",
    "A Máscara do Zorro", "A História do Pedro Coelho", "Fernão Capelo Gaivota", "Cinquenta Tons de Cinza", "Mensagem a Garcia",
    "O Mundo de Sofia", "O Jardim dos Esquecidos", "Anjos e Demônios", "Assim Foi Temperado O Aço", "Guerra e Paz", "As Aventuras de Pinóquio",
    "Você pode curar sua vida", "Seus Pontos Fracos", "O Falecido Grande Planeta Terra", "Caim e Abel", "Pássaros Feridos", "O Vale das Bonecas",
    "Em Seus Passos o Que Faria Jesus?", "O Sol é Para Todos", "O Símbolo Perdido", "E o Vento Levou", "Diário de Anne Frank", "Uma Vida com Propósitos",
    "The Revolt of Mamie Stover", "Os Homens que Não Amavam as Mulheres", "Uma Lagarta Muito Comilona"
]

titulos_disponiveis = Trie()
for livro in livros:
    titulos_disponiveis.inserir(livro)

prefixo_digitado = "Harry"
sugestoes = titulos_disponiveis.autocompletar(prefixo_digitado)
print(f"Sugestões com '{prefixo_digitado}':")
for sugestao in sugestoes:
    print(">> ", sugestao)
