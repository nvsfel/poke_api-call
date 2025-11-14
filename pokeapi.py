import re
import requests

def dex(poke):
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")
    dados = resposta.json()

    print("NATIONAL POKÉDEX\n\nPOKÉMON SUMMARY\n")
    print(f"Pokédex ID #{dados['id']}")
    print(f"Name: {dados['name'].title()}")
    print(f"Type: {dados['types'][0]['type']['name'].title()}")


    try:
        print(f"Secondary Type: {dados['types'][1]['type']['name'].title()}")
    except:
        pass
    print(f"Ability: {dados['abilities'][0]['ability']['name'].title()}\n\n")


    print(f"Height: {round(dados['height']/10, 2)}M.")
    print(f"Weight: {round(dados['weight']/10, 2)}KG.")

    print("Some Key-Moves:")
    for x in range(5):

        print(f"     {dados['moves'][x]['move']['name'].title()}")



    #link para foto:
    #print(dados['sprites']['other']['dream_world']['front_default'])

key = input("Type '1' to turn on the POKÉDEX.")

while(key == '1'):

    poke = input("Wich Pokémon do you want to research?\n")
    print(dex(poke))

    key = input("Type '1' to keep researching.")

print("POKÉDEX off.")

    
