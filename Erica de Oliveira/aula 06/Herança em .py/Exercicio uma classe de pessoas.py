

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome, self.idade, self.email = nome, idade, email

pessoa1 = Pessoa("erica", 33, "erica@exemplo.com")

print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("E-mail:", pessoa1.email)
