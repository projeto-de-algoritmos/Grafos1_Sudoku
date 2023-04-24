import pygame
import tkinter


def tela_vitoria():
    # Criando a janela
    root = tkinter.Tk()
    root.title("Parabéns")
    mensagem = "Parabéns você ganhou! :)"
    # Cria um label com a mensagem
    label = tkinter.Label(root, text=mensagem, pady=10)
    label.pack()
    # Cria um botão para fechar a janela
    button = tkinter.Button(root, text="OK", command=root.destroy)
    button.pack()
    root.geometry("300x100")
    # Define as coordenadas para o centro da tela
    root.update_idletasks()
    largura = root.winfo_width()
    altura = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (largura // 2)
    y = (root.winfo_screenheight() // 2) - (altura // 2)
    # Definindo posição do pop-up na tela
    root.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
    # Espera o usuário apertar no ok, após isso encerra o jogo
    root.mainloop()
    pygame.quit()
    exit()


def tela_resposta_errada():
    # Criando a janela
    root = tkinter.Tk()
    root.title("Você Consegue!")
    mensagem = "Resposta Incorreta :(\nTente mais um pouco!"
    # Cria um label com a mensagem
    label = tkinter.Label(root, text=mensagem, pady=10)
    label.pack()
    # Cria um botão para fechar a janela
    button = tkinter.Button(root, text="OK", command=root.destroy)
    button.pack()
    root.geometry("300x100")
    # Define as coordenadas para o centro da tela
    root.update_idletasks()
    largura = root.winfo_width()
    altura = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (largura // 2)
    y = (root.winfo_screenheight() // 2) - (altura // 2)
    # Definindo posição do pop-up na tela
    root.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
    root.mainloop()
