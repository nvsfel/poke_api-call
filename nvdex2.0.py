import tkinter as tk
from tkinter import ttk

##FUNÇÕES
def open_dex():

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
    approach_nat_dex.pack(ipadx=60, ipady=40)

    visor_nat_dex = tk.Entry(
        nat_dex,
        font=("arial",20),
        bd=8,
        justify="center"
        )
    visor_nat_dex.pack()

    botao_nat_dex = tk.Button(
        nat_dex,
        bd=8,
        text="GO!"
        )
    botao_nat_dex.pack(padx=20, pady=40)

    saida_nat_dex = tk.Listbox(
        nat_dex,
        bd=8,
        width=60,
        height=15,
        justify="center"
        )
    saida_nat_dex.pack(padx=60, pady=0)

    
    botao_hub = tk.Button(
        nat_dex,
        bd=8,
        text="HUB",
        command = nat_dex.destroy
        )
    botao_hub.pack(padx=60, pady=40)
    
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

abrir_dex = tk.Button(
    main_dex,
    command=open_dex,
    bd=8,
    text="OPEN DEX"
    )

abrir_dex.grid(row=0, column=1, columnspan=4)

fechar_dex = tk.Button(
    main_dex,
    command=main_dex.destroy,
    bd=8,
    text="CLOSE DEX"
    )
fechar_dex.pack(pady=10)
