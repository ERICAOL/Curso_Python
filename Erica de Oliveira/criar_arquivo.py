def criar_arquivo():
    nome_arquivo= "exemplo.txt"

    ## abre o arquivo no modo de escrita ('w')

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("este é um exemplo de arquivo criado com python.\n")
        arquivo.write("Você pode escrever várias linhas neste arquivo.\n")


if __name__== "__main__":
    criar_arquivo()
