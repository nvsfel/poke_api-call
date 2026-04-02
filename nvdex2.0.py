import requests
import random #sortear versões e moves
from functools import reduce #achatar listas

def moves(pokemon):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if resposta.status.code_code !=200:
        return "Movepool not found. Try again."

    dados_mov = resposta.json()
    moves = [] #declarar lista para preencher com a lista de moves
    moveset = [] #declarar lista para preencher com os moves tratados

    try:
        for x in range(311): #número baseado em Mew, pokémon com mais moves.
            moves.append(list({dados['moves'][x]['move']['name']}))
    except:
        pass

    moves = reduce(lambda x,y: x+y, moves)

    #selecionar 6 moves dentro da movepool completa

    
    for y in range(6):
        moveset.append(random.choice(moves))

    output_mov = ""
    output_mov += "Movepool:\n"
    for move in moveset:
        output_mov += f"{move.title()}\n"
        if moveset[1] == moveset[0]:
            break

    return output_mov
        
        


##FUNÇÕES DE INTERFACE

import tkinter as tk
from tkinter import ttk

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
main_dex.geometry("500x400+700+180")
main_dex.config(bg='#790d0d')

titulo = ttk.Label(
    main_dex,
    text="nvDEX",
    font=("Helvetica",15),
    foreground="#b3a125",
    anchor="center",
    background='#790d0d'
    )
titulo.pack(pady=30)

texto_main_dex = ttk.Label(
    main_dex,
    text = "HELLO TRAINER, WELCOME TO THE NATIONAL POKÉDEX",
    font =("Helvetica", 10),
    foreground="#b3a125",
    anchor="center",
    justify="center",
    background='#790d0d' 
    )
texto_main_dex.pack(pady=30)

abrir_dex = tk.Button(
    main_dex,
    command=open_dex,
    bd=8,
    text="OPEN DEX"
    )
abrir_dex.pack(pady=30)

fechar_dex = tk.Button(
    main_dex,
    command=main_dex.destroy,
    bd=8,
    text="CLOSE DEX"
    )
fechar_dex.pack(pady=30)
