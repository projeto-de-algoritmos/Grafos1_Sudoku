import pygame
import tkinter


def tela_vitoria():
    # Criando a janela
    pop_up = tkinter.Tk()
    pop_up.title("Parabéns")
    mensagem = "Parabéns você ganhou! :)"
    # Cria um label com a mensagem
    label = tkinter.Label(pop_up, text=mensagem, pady=10)
    label.pack()
    # Cria um botão para fechar a janela
    button = tkinter.Button(pop_up, text="OK", command=pop_up.destroy)
    button.pack()
    pop_up.geometry("300x100")
    # Define as coordenadas para o centro da tela
    pop_up.update_idletasks()
    largura = pop_up.winfo_width()
    altura = pop_up.winfo_height()
    x = (pop_up.winfo_screenwidth() // 2) - (largura // 2)
    y = (pop_up.winfo_screenheight() // 2) - (altura // 2)
    # Definindo posição do pop-up na tela
    pop_up.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
    # Espera o usuário apertar no ok, após isso encerra o jogo
    pop_up.mainloop()
    pygame.quit()
    exit()


def tela_resposta_errada():
    # Criando a janela
    pop_up = tkinter.Tk()
    pop_up.title("Você Consegue!")
    mensagem = "Resposta Incorreta :(\nTente mais um pouco!"
    # Cria um label com a mensagem
    label = tkinter.Label(pop_up, text=mensagem, pady=10)
    label.pack()
    # Cria um botão para fechar a janela
    button = tkinter.Button(pop_up, text="OK", command=pop_up.destroy)
    button.pack()
    pop_up.geometry("300x100")
    # Define as coordenadas para o centro da tela
    pop_up.update_idletasks()
    largura = pop_up.winfo_width()
    altura = pop_up.winfo_height()
    x = (pop_up.winfo_screenwidth() // 2) - (largura // 2)
    y = (pop_up.winfo_screenheight() // 2) - (altura // 2)
    # Definindo posição do pop-up na tela
    pop_up.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
    pop_up.mainloop()
