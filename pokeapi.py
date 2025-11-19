import requests 
import random #sortear versões e moves
from functools import reduce #achatar listas (turn to flat list)

def versoes():

    resposta_version = requests.get("https://pokeapi.co/api/v2/version")
    dados_version = resposta_version.json()

    versions = []
    for x in range(20):
        #descobri que são 20 versões printando todas.
        #todas as versões são trazidas em dicioários/sets.
        #aqui, os sets são transformados em listas, criando uma lista de listas.
        versions.append(list({dados_version['results'][x]['name']}))

    #nessa linha, cada versão, contida em uma lista dentro da lista maior,
    #é "dissolvida" em uma única lista com todas as versões.
    versions = reduce(lambda x,y: x + y, versions)
    versao_sorteada = random.choice(versions)


    return versao_sorteada
    #aparentemente, há versões que não contém determinados pokémon em suas entries.
    #implantar uma solução para isso, provavelmente try/except.

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

    versao = versoes()

    for entry in dados_entry['flavor_text_entries']:
        if entry['language']['name'] == 'en' and entry ['version']['name'] == versao:
            text = entry['flavor_text']
    text = text.replace('\n', ' ')
    print(f"\n{text}\n*this description comes from {versao.title()} version.")

def ability_entry(ability):

    resposta_ability = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}")
    dados_ability = resposta_ability.json()

    print(dados_ability['effect_entries'][1]['short_effect'] + '\n')


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
        print(f"\nHidden ability: {dados['abilities'][1]['ability']['name'].title()}\n")
        habs.append(dados['abilities'][1]['ability']['name'])
        ability_entry(habs[1])
    except:
        pass
              
    #peso e altura são dados em 
    print(f"Height: {round(dados['height']/10, 2)}M.")
    print(f"Weight: {round(dados['weight']/10, 2)}KG.")

    mov(poke)
    entry(poke)

#main:

key = input("Type '1' to turn on the POKÉDEX.\n")

while(key == '1'):

    poke = input("Which Pokémon do you want to research?\n")
    print(dex(poke))

    key = input("Type '1' to keep researching.\n")

print("POKÉDEX off.")

    
