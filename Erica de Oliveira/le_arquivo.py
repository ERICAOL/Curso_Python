
def ler_arquivo():
    nome_arquivo = "exemplo.txt"

    ## abre o arquivo no mode de leitura ( 'r')
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

if __name__== "__main__":
    ler_arquivo()
    