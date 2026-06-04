import requests
import random #sortear versões e moves
from functools import reduce #achatar listas
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO


def tecnicas(pokemon):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if resposta.status_code !=200:
        return "Something went wrong. Please try again."

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

        
    text += f"\n\n*description from {versao_selecionada.title()} version."
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
        return "Cannot recognize this Pokémon. Check your typing and try again."
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
    output_dex+="\n"
    try:
        output_dex+=descricao(pokemon) #importar descrição
    except:
        output_dex += "\n[Description could not be loaded.]"

    return output_dex

def pesquisar(visor_nat_dex):
    
    try:
        pokemon = visor_nat_dex.get()
        if pokemon == "":
            messagebox.showwarning("Warning","Enter pokémon name or number!",parent=nat_dex)
            return
    except:
        pass
    texto_dex = dex(visor_nat_dex)

    saida_nat_dex.config(state="normal")
    saida_nat_dex.delete("1.0", tk.END) #apagar o ultimo pokemon digitado após pesquisar
    saida_nat_dex.insert(tk.END, texto_dex) #escrever novos dados
    saida_nat_dex.config(state="disabled") #trancar a tela

                                   
        
def pegar_sprites():      

    pokemon = visor_nat_dex.get()
    resposta_imgs = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
    resposta=''
    resposta=resposta_imgs.json()
    extrair_frente = resposta['sprites']['other']['home']['front_default']

    link_frente = requests.get(extrair_frente)
    imgcrua_frente = BytesIO(link_frente.content)
    return imgcrua_frente
    
##FUNÇÕES DE INTERFACE

def screen_dex(event=None):
    screen_dex = tk.Toplevel()
    screen_dex.title("WORLDWIDE POKEDEX")
    screen_dex.geometry("500x700+700+180")
    screen_dex.config(bg='#790d0d')

    img_frentebruta = Image.open(pegar_sprites())
    img_frentelimpa = img_frentebruta.resize((250,250))
    sprite_frente = ImageTk.PhotoImage(img_frentelimpa)

    fotofrente = tk.Label(screen_dex)
    fotofrente.config(image=sprite_frente)
    fotofrente.image = sprite_frente

    fotofrente.pack(pady=20)

    

def open_dex(event=None):
    global nat_dex #como é uma aba subordinada, qualquer messagebox(e afins) necessita que o nat esteja globalizado
    nat_dex = tk.Toplevel()
    nat_dex.title("WORLDWIDE POKEDEX")
    nat_dex.geometry("500x700+700+180")
    nat_dex.bind("<Return>", lambda e: pesquisar(visor_nat_dex))
    nat_dex.bind("<KP_Enter>", lambda e: pesquisar(visor_nat_dex))
    nat_dex.config(bg='#790d0d')

    
    approach_nat_dex = tk.Label(
        nat_dex,
        text="Which creature do you want to research?",
        font =("Courier New", 10, "bold"),
        foreground="#b3a125",
        anchor="center",
        background='#212121',
        relief="sunken",
        bd=10
        )
    approach_nat_dex.pack(ipadx=12, ipady=20)


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
        font =("Verdana", 10),
        command = lambda: pesquisar(visor_nat_dex),
        bg="#fbc02d",
        fg="#000000",
        relief="flat",
        activebackground="#f57f14",
        activeforeground="#000000"
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

    botao_see = tk.Button(
        nat_dex,
        bd=8,
        text="SEE POKÉMON",
        font =("Verdana", 10),
        command = screen_dex,
        bg="#fbc02d",
        fg="#000000",
        relief="flat",
        activebackground="#f57f14",
        activeforeground="#000000"
        )
    botao_see.pack(padx=60, pady=20)

    
    botao_hub = tk.Button(
        nat_dex,
        bd=8,
        text="HUB",
        font =("Verdana", 10),
        command = nat_dex.destroy,
        bg="#fbc02d",
        fg="#000000",
        relief="flat",
        activebackground="#f57f14",
        activeforeground="#000000"
        )
    botao_hub.pack(padx=60, pady=20)



def fechar_dex():
    fechar = messagebox.askyesno(
        "Warning",
        "Do you want really to close the Dex?",
        default=messagebox.NO,
        parent=main_dex
        )
    if fechar:
        main_dex.destroy()
    


##INTERFACE
    
main_dex = tk.Tk()
main_dex.title("WORLDWIDE POKÉDEX")
main_dex.geometry("500x400+700+180") #proporções
main_dex.bind("<Return>", open_dex)
main_dex.bind("<KP_Enter>", open_dex)
main_dex.config(bg='#790d0d')

titulo = tk.Label(
    main_dex,
    text="nvDEX",
    font=("Helvetica",15),
    foreground="#b3a125",
    anchor="center",
    background='#790d0d'
    )
#titulo.pack(pady=30) suspenso

texto_main_dex = tk.Label(
    main_dex,
    text = "HELLO TRAINER, WELCOME TO THE WORLDWIDE POKÉDEX",
    font =("Courier New", 10),
    foreground="#b3a125",
    anchor="center",
    justify="center",
    background='#212121',
    relief="sunken",
    bd=4
    )
texto_main_dex.pack(pady=40)

abrir_dex = tk.Button(
    main_dex,
    command=open_dex,
    bd=8,
    text="OPEN DEX",
    font =("Verdana", 10),
    bg="#fbc02d",
    fg="#000000",
    relief="flat",
    activebackground="#f57f14",
    activeforeground="#000000"
    )
abrir_dex.pack(pady=30)

fechar_dex = tk.Button(
    main_dex,
    command=fechar_dex,
    bd=8,
    text="CLOSE DEX",
    font =("Verdana", 10),
    bg="#fbc02d",
    fg="#000000",
    relief="flat",
    activebackground="#f57f14",
    activeforeground="#000000"
    )
fechar_dex.pack(pady=30)



main_dex.mainloop()
