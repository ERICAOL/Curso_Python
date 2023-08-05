

import tkinter as tk
from PIL import Image, ImageTk


def main():
    janela = tk.Tk()
    janela.title("Exemplo de inserção de imagem")
    image = Image.open("300.jpg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(janela, image=photo) # Criando rótulo para exibir a imangem
    label.pack()
    
    janela.mainloop()
if __name__ == "__main__":
    main()
