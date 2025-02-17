import ipaddress

class No_Trie:
    def __init__(self):
        self.filhos = {}
        self.prefixo = None

class Trie:
    def __init__(self):
        self.raiz = No_Trie()

    def inserir(self, prefixo):
        network = ipaddress.ip_network(prefixo, strict=False)
        octetos = str(network.network_address).split('.')[:network.prefixlen // 8]
        no = self.raiz
        for octeto in octetos:
            if octeto not in no.filhos:
                no.filhos[octeto] = No_Trie()
            no = no.filhos[octeto]
        no.prefixo = prefixo

    def maior_prefixo_encontrado(self, ip):
        octetos = str(ipaddress.ip_address(ip)).split('.')
        no = self.raiz
        maior_encontrado = None
        for octeto in octetos:
            if octeto in no.filhos:
                no = no.filhos[octeto]
                if no.prefixo:
                    maior_encontrado = no.prefixo
            else:
                break
        return maior_encontrado

trie = Trie()
prefixos = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
for prefixo in prefixos:
    trie.inserir(prefixo)

ip = "192.168.1.100"
print(f"Maior prefixo encontrado para {ip}: {trie.maior_prefixo_encontrado(ip)}")
