from tkinter import *

janela = Tk()
janela.title("Formulário de cadastro")
janela.geometry("500x400+500+200")
janela.config(bg="gray")

lblNome = Label(janela,text= "Nome", width=8, font= "arial")
lblNome.place(x=100, y=100)
txtNome = Entry(janela, text="", width=20, font = "arial").place(x=200, y=100)

janela.mainloop()