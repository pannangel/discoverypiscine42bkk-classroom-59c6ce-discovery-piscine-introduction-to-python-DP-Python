#!/usr/bin/env python3
person = { "James" : "Wilson",
   "Michale" : "Jackson",
   "John" : "Wick",
   "Steve" : "Jobs"
}

def array_of_names(persons):
    full_names = []
    for first, last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

print(array_of_names(person))