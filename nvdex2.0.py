import tkinter as tk
from tkinter import ttk

##FUNÇÕES
def open_dex():

    nat_dex = tk.Toplevel()
    nat_dex.title("NATIONAL DEX")

    


##INTERFACE
    
main_dex = tk.Tk()
main_dex.title("NVDEX")
    #proporções
main_dex.geometry("500x700+700+180")

titulo = ttk.Label(
    main_dex,
    text="nvDEX",
    font=("Poke",15),
    anchor="center",
    )
titulo.pack(ipadx=60, ipady=40)

texto_main_dex = ttk.Label(
    main_dex,
    text = "HELLO TRAINER, WELCOME TO THE NATIONAL POKÉDEX",
    font =("Helvetica", 10),
    anchor="center",
    justify="center",
    )
texto_main_dex.pack(ipadx=20, ipady=10)

abrir_dex = tk.Button(main_dex, command=open_dex, text="OPEN DEX")
abrir_dex.pack(pady=10)

fechar_dex = tk.Button(main_dex, command=main_dex.destroy, text="CLOSE DEX")
fechar_dex.pack(pady=10)
