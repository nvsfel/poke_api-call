import re
import requests

def dex(poke):
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")

    if resposta.status_code == 404:
        return "Pokémon not found. Check your typing and try again."
    elif resposta.status_code != 200:
        return "Something went wrong. Try again."

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

    print("\nSome Key-Moves:")

    try:
        for x in range(6):

            print(f"     {dados['moves'][x]['move']['name'].title()}")
    except:
        pass
    

    #link para foto:
    #print(dados['sprites']['other']['dream_world']['front_default'])

key = input("Type '1' to turn on the POKÉDEX.\n")

while(key == '1'):

    poke = input("Which Pokémon do you want to research?\n")
    print(dex(poke))
    
    

    key = input("Type '1' to keep researching.\n")

print("POKÉDEX off.")

    
