

def criar_arquivo():
    nome_arquivo = "exemplo.txt"

with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

if __name__ == "__mais__":
    ler_arquivo()