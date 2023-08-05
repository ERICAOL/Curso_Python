######################### Sistema de controle de faltas#####################
#Escreva um programa que receba uma entrada de usuarios sobre a quantidade de faltas que possui. 
###Usuario so pode ter 25% de falta de um total de 80h para ser aprovado


quantidade_faltas = int(input("Digite a quantidade de faltas que possui:"))

if(quantidade_faltas<= 0.25*80):
    print("Voce esta dentro do limite de faltas.")
else:
    print("Voce excedeu o limite de faltas.")