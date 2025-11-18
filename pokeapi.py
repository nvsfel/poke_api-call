import requests

def entry(poke):

    #chamada secundária (descrição de pokémon)
    resposta_entry = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{poke}")
    #resposta atribuída a 'dados_entry'
    dados_entry = resposta_entry.json()

   
    #dissecando a resposta da chamada:
    for entry in dados_entry['flavor_text_entries']:

        #separando exclusivamente respostas na 'linguagem''nome' == inglês
        #e 'versão''nome' == red
        if entry['language']['name'] == 'en' and entry ['version']['name'] == 'red':
            text = entry['flavor_text']
    text = text.replace('\n', ' ')
    print(text + '\n')




def dex(poke):

    #chamada principal (busca pokémon)
    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")

    #resposta para erro de digitação
    if resposta.status_code == 404:
        return "Pokémon not found. Check your typing and try again."
    #resposta generalista para outros erros
    elif resposta.status_code != 200:
        return "Something went wrong. Try again."

    #resposta da busca principal atibuída a 'dados'
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
    print(f"Ability: {dados['abilities'][0]['ability']['name'].title()}\n\n")

    #peso e altura são dados em 
    print(f"Height: {round(dados['height']/10, 2)}M.")
    print(f"Weight: {round(dados['weight']/10, 2)}KG.")

    print("\nSome Key-Moves:")

    # moveset + prevenção para pokémons com menos de 6 moves
    try:
        for x in range(6):

            print(f"     {dados['moves'][x]['move']['name'].title()}")
    except:
        pass

    #descrição do pokémon

    entry(poke)
    
#main:

key = input("Type '1' to turn on the POKÉDEX.\n")

while(key == '1'):

    poke = input("Which Pokémon do you want to research?\n")
    print(dex(poke))
    
    

    key = input("Type '1' to keep researching.\n")

print("POKÉDEX off.")

    
