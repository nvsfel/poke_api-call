import requests 
import random #sortear versões e moves
from functools import reduce #achatar listas (turn to flat list)

def mov(pokemon):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if resposta.status_code != 200:
        return "Movepool not found. Try again."
    dados = resposta.json()
    moves = [] #declarar lista para preencher com a lista de listas de moves
    moveset = [] #declarar lista para preencher com os moves tratados
    try:
        for x in range(311): #número baseado em Mew, pokémon com mais moves.
            moves.append(list({dados['moves'][x]['move']['name']}))
    except:
        pass
    moves = reduce(lambda x,y: x+y, moves)

    for y in range(6):
        moveset.append(random.choice(moves))

    output_mov = ''
    output_mov += "Movepool:\n"
    for move in moveset:
        output_mov += f"    {move.title()}\n"
        if moveset[1] == moveset[0]: #contenção para pokémons com apenas 1 ataque.
            break

    return output_mov

def entry(pokemon):

    resposta_entry = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
    
    dados_entry = resposta_entry.json()
    
    text = 'Pokémon description not found.' #Texto de garantia
    versoes_validas = []

    #FILTRAGEM DE VERSÕES VÁLIDAS (em inglês) PARA {poke}, o pokémon pesquisado.
    for entry in dados_entry['flavor_text_entries']:
        if entry['language']['name'] == 'en': 
            versoes_validas.append(entry['version']['name'])
            #anexa nessa variável apenas versões em que há entry para o pokémon pesquisado. 'red','violet' etc.

    versao_selecionada = random.choice(versoes_validas)

    #Dentre todos os dados de descrição, esse loop, através da condicional, compara o dado de descrição
    #com o da versão selecionada em inglês..
    for entry in dados_entry['flavor_text_entries']:
        if entry['language']['name'] == 'en' and entry['version']['name'] == versao_selecionada:
            text = f"\n{entry['flavor_text']}"
            break
    text = text.replace('','')
    text += f"\n\n*description from {versao_selecionada.title()} version."
    return text

def ability_entry(ability):

    resposta_ability = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}")
    dados_ability = resposta_ability.json()

    output_ability = ''
    try:
        output_ability = dados_ability['effect_entries'][1]['short_effect'] + '\n'
    except:
        pass
    return output_ability

def dex(poke):

    pokemon = poke.get()
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if resposta.status_code == 404:
        return "Pokémon not found. Check your typing and try again."
    elif resposta.status_code != 200:
        return "Something went wrong. Try again."
    dados = resposta.json()

    #Sumário
    output_dex = ''
    output_dex+= "NATIONAL POKÉDEX\n\nPOKÉMON SUMMARY\n"
    output_dex+= f"Pokédex ID #{dados['id']}\n"
    output_dex+= f"Name: {dados['name'].title()}\n"
    output_dex+= f"Type: {dados['types'][0]['type']['name'].title()}\n"

    #caso para pokémons com 2 tipos:
    try:
        output_dex+= f"Secondary Type: {dados['types'][1]['type']['name'].title()}\n"
    except:
        pass

    #habilidade
    output_dex+= f"\nAbility: {dados['abilities'][0]['ability']['name'].title()}\n"
    habs = [dados['abilities'][0]['ability']['name']]
    output_dex+=ability_entry(habs[0])
    try:
        output_dex+= f"Hidden ability: {dados['abilities'][1]['ability']['name'].title()}\n"
        habs.append(dados['abilities'][1]['ability']['name']+'\n')
        output_dex+=ability_entry(habs[1])
        
    except:
        pass
    #peso e altura são dados em hectogramas e em decímetros, respectivamente.
    output_dex+= f"Height: {round(dados['height']/10, 2)}M.\n"
    output_dex+= f"Weight: {round(dados['weight']/10, 2)}KG.\n\n"
    
    
    output_dex+=mov(pokemon) #importar moveset
    try:
        output_dex+=entry(pokemon) #importar descrição
    except:
        output_dex += "\n[Description could not be loaded.]"

    return output_dex


def pesquisar():

    pokemon = poke.get()

    texto_dex = dex(poke)

    output.config(text=texto_dex)
    
       
 
#main:

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#estrutura da janela
pokedex = tk.Tk()
pokedex.title("NVDEX")
#proporções
pokedex.geometry("500x700+700+180")
pokedex.maxsize(600,1050)
pokedex.minsize(250,350)

pokedex.config(bg='#460000')
pokedex.iconbitmap('C:/Users/202503536521/Downloads/nvdex/assets/pokeb.ico')
 #imagem precisa estar na mesma pasta do código, ou aqui precisa ter o caminho do arquivo.

#tela da dex:
def tela():
    tela_dex = tk.Toplevel()
    tela_dex.title("DEXSCREEN")
    tela_dex.geometry("500x700+700+180")
    tela_dex.maxsize(600,1050)
    tela_dex.minsize(250,350)
    tela_dex.config(bg='#460000')
    tela_dex.iconbitmap('C:/Users/202503536521/Downloads/nvdex/assets/pokeb.ico')
    #"lambda event: tela()"

 #cabeçalho da janela



titulo = ttk.Label(
    pokedex,
    text="    nvDEX    ",
    font=("Arial", 15),
    foreground='white',
    background='#7d0000',
    anchor="center",
    borderwidth=3,
    relief="groove"
)
titulo.pack(ipadx=60,ipady=40)

text_poke = ttk.Label(
    pokedex,
    text = "Which Pokémon do you want to research?",
    font=("Arial", 10),
    foreground="white",
    background="#460000",
    anchor="center"
    )
text_poke.pack(ipadx = 20, ipady=10)

poke = ttk.Entry(pokedex)
poke.pack(pady=10)

img_original = Image.open('C:/Users/202503536521/Downloads/nvdex/assets/pokeb.png')
img_tratada = img_original.resize((50,50))

botao_imagem = ImageTk.PhotoImage(img_tratada)

botao_pesquisar = tk.Button(pokedex, image=botao_imagem, command = pesquisar, bg="#460000")
botao_pesquisar.pack(pady=10)

output = ttk.Label(
    pokedex,
    text= "Waiting for research...",
    font=("Arial", 10),
    foreground="white",
    background="#460000",
    anchor="center"
)
output.pack()

pokedex.mainloop()
