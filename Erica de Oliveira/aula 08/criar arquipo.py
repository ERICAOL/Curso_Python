



def criar_arquivo():
    nome_arquivo= "exemplo.txt"


#Abre o arquivo no modo de escrita ('w')

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Este é um exemplo de arquivo criado com Python.\n")
        arquivo.write("Você pode escrever várias linhas neste arquivo.\n")

if __name__ == "__mais__":
    criar_arquivo()