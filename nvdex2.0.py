import requests
import random #sortear versões e moves
from functools import reduce #achatar listas

def tecnicas(pokemon):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if resposta.status_code !=200:
        return "Movepool not found. Try again."

    dados_mov = resposta.json()
    moves = [] #declarar lista para preencher com a lista de moves
    moveset = [] #declarar lista para preencher com os moves tratados

    try:
        for x in range(311): #número baseado em Mew, pokémon com mais moves.
            moves.append(list({dados_mov['moves'][x]['move']['name']}))
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

def descricao(pokemon):

    resposta_entry = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")

    dados_entry = resposta_entry.json()

    text = ' Pokémon description not found.' #Verificação p/ erro

    versoes_validas = []

    for entry in dados_entry['flavor_text_entries']:
        if entry['language']['name'] == 'en':
            versoes_validas.append(entry['version']['name'])

    versao_selecionada = random.choice(versoes_validas)

    #Dentre todos os dados de descrição, esse loop, através da condicional, compara o dado de descrição
    #com o da versão selecionada em inglês..

    for entry in dados_entry['flavor_text_entries']:
        if entry['language']['name'] == 'en' and entry['version']['name'] == versao_selecionada:
            text = f"{entry['flavor_text']}"
            break

        text = text.replace('','')
        text += f"\n*description from {versao_selecionada.title()} version."
        return text

def habilidade_entry(habilidade):

    resposta_habilidade = requests.get(f"https://pokeapi.co/api/v2/ability/{habilidade}")
    dados_habilidade = resposta_habilidade.json()

    output_habilidade = ''

    try:
        output_habilidade = dados_habilidade['effect_entries'][2]['short_effect'] + '\n'

    except:
        pass

    return output_habilidade

def dex(pokemon_pesquisado):
    
    pokemon = pokemon_pesquisado.get()
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    #verificação de erro

    mensagens_erro = ['What is Team Rocket plotting now?','Is there a nearby Pokémon tricking us?', 'The internet connection in this Region is oscillating... Bad sign.']
    mensagem_da_vez = random.choice(mensagens_erro)

    if resposta.status_code ==404:
        return "Pokémon not found. Check your typing and try again."
    elif resposta.status_code != 200:
        return "Something went wrong. {mensagem_da_vez}"

    dados = resposta.json()

    output_dex = ''
    output_dex+= "NATIONAL POKÉDEX\n\nPOKÉMON SUMMARY\n"
    output_dex+= f"Pokédex ID #{dados['id']}\n"
    output_dex+= f"Name: {dados['name'].title()}\n"
    output_dex+= f"Type: {dados['types'][0]['type']['name'].title()}\n"

    try:
        output_dex+= f"Secondary Type: {dados['types'][1]['type']['name'].title()}\n"
    except:
        pass

    output_dex+= f"\nAbility: {dados['abilities'][0]['ability']['name'].title()}\n"
    habs = [dados['abilities'][0]['ability']['name']]
    output_dex+=habilidade_entry(habs[0])
    try:
        output_dex+= f"Hidden ability: {dados['abilities'][1]['ability']['name'].title()}\n"
        habs.append(dados['abilities'][1]['ability']['name']+'\n')
        output_dex+=habilidade_entry(habs[1])
        
    except:
        pass
    #peso e altura são dados em hectogramas e em decímetros, respectivamente.
    output_dex+= f"Height: {round(dados['height']/10, 2)}M.\n"
    output_dex+= f"Weight: {round(dados['weight']/10, 2)}KG.\n\n"
    
    
    output_dex+=tecnicas(pokemon) #importar moveset
    try:
        output_dex+=habilidade_entry(pokemon) #importar descrição
    except:
        output_dex += "\n[Description could not be loaded.]"

    return output_dex

def pesquisar(visor_nat_dex):
    
    pokemon = visor_nat_dex.get()

    texto_dex = dex(visor_nat_dex)

    saida_nat_dex.config(state="normal")
    saida_nat_dex.delete("1.0", tk.END) #apagar o ultimo pokemon digitado após pesquisar
    saida_nat_dex.insert(tk.END, texto_dex) #escrever novos dados
    saida_nat_dex.config(state="disabled") #trancar a tela

                                   
        
        


##FUNÇÕES DE INTERFACE

import tkinter as tk
from tkinter import ttk

def open_dex(event=None):

    nat_dex = tk.Toplevel()
    nat_dex.title("NATIONAL DEX")
    nat_dex.geometry("500x700+700+180")
    nat_dex.bind("<Return>", lambda e: pesquisar(visor_nat_dex))
    nat_dex.bind("<KP_Enter>", lambda e: pesquisar(visor_nat_dex))
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


    global visor_nat_dex
    visor_nat_dex = tk.Entry(
        nat_dex,
        font=("Verdana",20),
        bd=8,
        justify="center"
        )
    
    visor_nat_dex.pack()

    botao_nat_dex = tk.Button(
        nat_dex,
        bd=8,
        text="GO!",
        command = lambda: pesquisar(visor_nat_dex)
        #linha que possibilita o bind (usar o enter como "clique" em função com parametro)
        )
    botao_nat_dex.pack(padx=20, pady=40)

    global saida_nat_dex
    saida_nat_dex = tk.Text(
        nat_dex,
        font="Verdana",
        bd=8,
        width=60,
        height=15        
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
main_dex.geometry("500x400+700+180") #proporções
main_dex.bind("<Return>", open_dex)
main_dex.bind("<KP_Enter>", open_dex)
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



main_dex.mainloop()
