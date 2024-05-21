import json

def save_json(file='', card='', nome='', info='', element='', eff='', mana='', power='', idate='', frame=''):
    final_file = f'{file}'
    dictionary = {
        'Card': f'{card}',
        'Name': f'{nome}',
        'Card Info': f'{info}',
        'Effect': f'{eff}',
        'Card Element': f'{element}',
        'Mana Cost': f'{mana}',
        'Card Power': f'{power}',
        'Card ID/Date': f'{idate}',
        'Card Frame': f'{frame}'
    }
    with open(f"{final_file}.json", "w") as outfile:
        json.dump(dictionary, outfile)
