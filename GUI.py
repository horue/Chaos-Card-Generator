import tkinter
from GUI_variables import v, pv
from tkinter import ttk

def guistart():
    root = tkinter.Tk()
    root.title(f"Chaos Card Generator - {v}")
    root.resizable(True, True)


    label = tkinter.Label(root, text="")
    label.pack()

    label = tkinter.Label(root, text=f"GUI - {pv}")
    label.pack()

    #Escolha o nome da carta

    label = tkinter.Label(root, text="")
    label.pack()

    label = tkinter.Label(root, text="Nome:")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    label = tkinter.Label(root, text="")
    label.pack()

    #Escolha o elemento da carta

    label = tkinter.Label(root, text="Tipo da Criatura:")
    label.pack()

    n = tkinter.StringVar()
    escolha = ttk.Combobox(root, textvariable = n)
    escolha.pack()
    escolha['values'] = ('Água','Fogo','Terra', 'Vento', 'Luz', 'Trevas')

    #Escolha do tipo de moldura carta

    label = tkinter.Label(root, text="")
    label.pack()

    label = tkinter.Label(root, text="Tipo de Moldura:")
    label.pack()

    n = tkinter.StringVar()
    escolha = ttk.Combobox(root, textvariable = n)
    escolha.pack()
    escolha['values'] = (' Full Art',' Arte Estendida',' Arte Especial')

    label = tkinter.Label(root, text="")
    label.pack()


    #Definição geral dos botões do programa


    quit = tkinter.Button(root, text="SAIR", command=root.destroy)
    quit.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs



guistart()