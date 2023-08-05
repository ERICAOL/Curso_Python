

class Pessoa:
    def __init__(pessoa, nome, idade, e_mail, endereco):
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.e_mail = e_mail
        pessoa.endereco = endereco

    def imprimir_dados(pessoa):
        print("nome:", pessoa.nome)
        print("idade:", pessoa.idade)
        print("e_mail:", pessoa.e_mail)
        print("endereco", pessoa.endereco)

Cliente01 = Pessoa ("erica", 33 , "ricaa.oliveiraa@gmail.com", "Ipiranga")
Cliente01.imprimir_dados()


class cachorro:
    def __init__(cachorro, nome, porte, raça, idade):
        cachorro.nome = nome
        cachorro.porte = porte
        cachorro.raça = raça
        cachorro.idade = idade

    def imprimir_dados(cachorro):
        print("nome:", cachorro.nome)
        print("porte:", cachorro.porte)
        print("raça:", cachorro.raça)
        print("idade:", cachorro.idade)

Animal = cachorro ("luana", "médio", "vira lata", 6)
Animal.imprimir_dados()


