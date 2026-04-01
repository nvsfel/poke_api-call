import tkinter as tk
from tkinter import ttk

##FUNÇÕES
def open_dex():

    main_dex.destroy()#abre uma janela 'tk' vazia
    nat_dex = tk.Toplevel()
    nat_dex.title("NATIONAL DEX")
    nat_dex.geometry("500x700+700+180")

    nat_dex.config(bg='#790d0d')

    
    approach_nat_dex = ttk.Label(
        nat_dex,
        text="Which Creature do you want to Research?",
        font=("Helvetica",15),
        foreground="#b3a125",
        anchor="center",
        background='#790d0d'
        )
    nat_dex.pack(ipadx=60, ipady=40)

    entry_nat_dex = ttk.Entry
    #trazer entries



##INTERFACE
    
main_dex = tk.Tk()
main_dex.title("NVDEX")
    #proporções
main_dex.geometry("500x700+700+180")
main_dex.config(bg='#790d0d')

titulo = ttk.Label(
    main_dex,
    text="nvDEX",
    font=("Helvetica",15),
    foreground="#b3a125",
    anchor="center",
    background='#790d0d'
    )
titulo.pack(ipadx=60, ipady=40)

texto_main_dex = ttk.Label(
    main_dex,
    text = "HELLO TRAINER, WELCOME TO THE NATIONAL POKÉDEX",
    font =("Helvetica", 10),
    foreground="#b3a125",
    anchor="center",
    justify="center",
    background='#790d0d' 
    )
texto_main_dex.pack(ipadx=20, ipady=10)

abrir_dex = tk.Button(main_dex, command=open_dex, text="OPEN DEX")
abrir_dex.pack(pady=10)

fechar_dex = tk.Button(main_dex, command=main_dex.destroy, text="CLOSE DEX")
fechar_dex.pack(pady=10)
