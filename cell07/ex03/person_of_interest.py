#!/usr/bin/env python3
def famous_births(scientists_dict):
    sorted_scientists = sorted(scientists_dict.items(), key=lambda x: x[1]["date_of_birth"])
    for key, person in sorted_scientists:
        name = person["name"]
        birth_date = person["date_of_birth"]
        print(f"{name} is a great scientist born in {birth_date}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)