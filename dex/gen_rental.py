import json

full_file = "dex/johto.json"
rental_ref = "dex/stadium2_rental.txt"
out_file = "dex/stadium2.json"

with open(full_file, "r") as file:
    full_dex = json.load(file)

new_dex = dict()

with open(rental_ref, "r", encoding="UTF-8") as file:
    rental_str = file.read()

rental_split = rental_str.split("#")

for i, pokemon in enumerate(rental_split[1:]):
    lines = pokemon.split("\n")
    id = int(lines[0].split()[0])
    name = lines[1].replace(" ", "")
    hp = int(lines[5].split('\t')[1])
    attack = int(lines[6].split('\t')[1])
    defense = int(lines[7].split('\t')[1])
    if len(lines) == 17:
        special_attack = int(lines[8].split('\t')[1])
        special_defense = int(lines[9].split('\t')[1])
        speed = int(lines[10].split('\t')[1])
        moves = lines[12:16]
        pokedict = dict(id=i, dex_id=id, name=name, hp=hp, attack=attack, defense=defense, special_attack=special_attack, special_defense=special_defense, speed=speed, moves=moves)
    else:
        special = int(lines[8].split('\t')[1])
        speed = int(lines[9].split('\t')[1])
        moves = lines[11:15]
        pokedict = dict(id=i, dex_id=id, name=name, hp=hp, attack=attack, defense=defense, special=special, speed=speed, moves=moves)
    new_dex[name] = pokedict

final_dex = []

for pokemon in full_dex:
    key = pokemon['name'].replace(' ','')
    if key not in new_dex.keys():
        continue
    rental_entry = new_dex[key]
    for k, v in rental_entry.items():
        if k == "id":
            continue
        pokemon[k] = v
    final_dex.append(pokemon)

with open(out_file, "w") as file:
    json.dump(final_dex, file)
