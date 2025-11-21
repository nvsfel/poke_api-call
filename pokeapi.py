import requests 
import random #sortear versões e moves
from functools import reduce #achatar listas (turn to flat list)

def mov(poke):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")
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

    print("Some Key-Moves:\n") 
    for move in moveset:
        print(f"    {move.title()}")
        if moveset[1] == moveset[0]: #contenção para pokémons com apenas 1 ataque.
            break

def entry(poke):

    resposta_entry = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{poke}")
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
            text = entry['flavor_text']
            break
    text = text.replace('\n', ' ')
    text = text.replace('','') 
    print(f"\n{text}\n*description from {versao_selecionada.title()} version.")        

def ability_entry(ability):

    resposta_ability = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}")
    dados_ability = resposta_ability.json()
    try:
        print(dados_ability['effect_entries'][1]['short_effect'] + '\n')
    except:
        pass

def dex(poke):

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")
    if resposta.status_code == 404:
        return "Pokémon not found. Check your typing and try again."
    elif resposta.status_code != 200:
        return "Something went wrong. Try again."
    dados = resposta.json()

    #Sumário
    print("NATIONAL POKÉDEX\n\nPOKÉMON SUMMARY\n")
    print(f"Pokédex ID #{dados['id']}")
    print(f"Name: {dados['name'].title()}")
    print(f"Type: {dados['types'][0]['type']['name'].title()}")

    #caso para pokémons com 2 tipos:
    try:
        print(f"Secondary Type: {dados['types'][1]['type']['name'].title()}")
    except:
        pass

    #habilidade
    print(f"\nAbility: {dados['abilities'][0]['ability']['name'].title()}\n")
    habs = [dados['abilities'][0]['ability']['name']]
    ability_entry(habs[0])
    try:
        print(f"Hidden ability: {dados['abilities'][1]['ability']['name'].title()}\n")
        habs.append(dados['abilities'][1]['ability']['name'])
        ability_entry(habs[1])
    except:
        pass
    #peso e altura são dados em hectogramas e em decímetros, respectivamente.
    print(f"Height: {round(dados['height']/10, 2)}M.")
    print(f"Weight: {round(dados['weight']/10, 2)}KG.")
    
    mov(poke) #importar moveset
    try:
        entry(poke) #importar descrição
    except:
        pass
#main:

key = input("Type '1' to turn on the POKÉDEX.\n")

while(key == '1'):
    poke = input("Which Pokémon do you want to research?\n")
    print(dex(poke))
    key = input("Type '1' to keep researching.\n")
print("POKÉDEX off.")
