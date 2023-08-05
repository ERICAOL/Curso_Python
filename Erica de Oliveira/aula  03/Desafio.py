Escreva um programa que recebe uma lista de números  do usuário e retorne a soma

"""numeros = [int(num)for num in numeros]

print("A soma dos números é: , soma")""""""

"""numeros= [int(num) for num in numeros]1
print(numeros)"""

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]
soma = 0
for elemento in numeros:
    soma = soma + elemento
    
print(soma)
