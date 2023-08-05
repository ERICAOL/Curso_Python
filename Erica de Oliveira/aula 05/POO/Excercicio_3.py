
def saudação(nome):
    nome = input(input("Digite seu nome"))
    print("Ola", nome, "Bem vindo ao seu banco")
    
class conta_bancaria:

    def __init_subclass__(conta_bancaria, agencia, valor_conta):
        conta_bancaria.agencia = agencia
        conta_bancaria.valor_conta = valor_conta

Cliente01 = conta_bancaria ("10", "500")
Cliente01.imprimir_dados()

def __init__(conta_bancaria, titular,saldo=0):
        conta_bancaria.titular = titular
        conta_bancaria.saldo = saldo
        
def depositar(conta_bancaria):
        valor = int(input("Digite um valor a depositar: "))
        conta_bancaria.saldo += valor
    
    
def sacar(conta_bancaria):
        valor = int(input("Deseja depositar qual valor"))
        if valor <= conta_bancaria.saldo:
            conta_bancaria.saldo = valor
        else: 
            print("Saldo insuficiente")

def imprimir_saldo(conta_bancaria):
        print("Nome: ", conta_bancaria.titular)
        print("Saldo: ",conta_bancaria.saldo)


        

        
