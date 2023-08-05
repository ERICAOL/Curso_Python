

class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar(self):
        print("Veiculo acelerou")


class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca

    def ligar(self):
        print("O carro ligou")



