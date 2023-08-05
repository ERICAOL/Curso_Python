##Faça um programa no qual o usuario possa adicionar nome do contato, telefone e imprima Valor


#Exercício agenda telefônica

agenda_telefonica = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de e-mail: ")
    contato = {'telefone': telefone, 'email': email}
    agenda_telefonica[nome] = contato
    print("Contato adicionado com sucesso!")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in agenda_telefonica:
        del agenda_telefonica[nome]
        print("Contato apagado com sucesso!")
    else:
        print("Contato não encontrado!")

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    if nome in agenda_telefonica:
        telefone = input("Digite o novo número de telefone: ")
        email = input("Digite o novo endereço de e-mail: ")
        contato = {'telefone': telefone, 'email': email}
        agenda_telefonica[nome] = contato
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado!")

def visualizar_contatos():
    if agenda_telefonica:
        print("Lista telefônica:")
        for nome, contato in agenda_telefonica.items():
            print(f"Nome: {nome}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")
            print()
    else:
        print("A lista telefônica está vazia!")

while True:
    print("\nSelecione uma opção:")
    print("1. Adicionar contato")
    print("2. Apagar contato")
    print("3. Atualizar contato")
    print("4. Mostrar contatos")
    print("0. Sair")

    opcao = input("Opção selecionada: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        apagar_contato()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        mostrar_contatos()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

print("Programa encerrado.")
