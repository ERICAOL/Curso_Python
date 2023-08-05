from tkinter import *

janela = Tk()
janela.title("Formulário de Cadastro")

# Largura x Altura + Distância margem esquerda + Distância topo
janela.geometry("500x500+500+200")

# Definindo a cor do fundo da tabela
janela.config(bg="gray")

# Labels

lblNome = Label(janela, text="Nome", width=8, font="arial")
lblNome.place(x=100, y=100)  # coordenada de localização
txtNome = Entry(janela, text="", width=20, font="arial")
txtNome.place(x=200, y=100)

lblEmail = Label(janela, text="E-mail", width=8, font="arial")
lblEmail.place(x=100, y=150)
txtEmail = Entry(janela, text="", width=20, font="arial")
txtEmail.place(x=200, y=150)

lblTelefone = Label(janela, text="Telefone", width=8, font="arial")
lblTelefone.place(x=100, y=200)
txtTelefone = Entry(janela, text="", width=20, font="arial")
txtTelefone.place(x=200, y=200)

lblCPF = Label(janela, text="CPF", width=8, font="arial")
lblCPF.place(x=100, y=250)
txtCPF = Entry(janela, text="", width=20, font="arial")
txtCPF.place(x=200, y=250)

# Botões

def Enviar():
    lblResultado["text"] = "Dados Enviados com sucesso!"
    txtNome.delete(0, END)
    txtCPF.delete(0, END)
    txtEmail.delete(0, END)
    txtTelefone.delete(0, END)

btnEnviar = Button(janela, text="Enviar", width=20, command=Enviar, font="arial")
btnEnviar.place(x=100, y=300)

lblResultado = Label(janela, text="Resultado", width=20, font="arial")
lblResultado.place(x=100, y=350)

janela.mainloop()
