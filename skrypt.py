

import itertools
from typing import Dict


required_keys = ("first_name__last_name", "first_name__age")
inp = {
            "first_name": "Jan",
            "last_name": "Kowalski",
            "age": "18",
        }

splitted_words = []
after_split = []
without_split = []
for key in required_keys:
    if "__" in key:
        after_split.append(key.split("__"))
        splitted_words.append(key)
    else:
        without_split.append(key)

if len(without_split) > 1:
    prepared_args = list(itertools.chain(*without_split, *after_split))
else:
    prepared_args = list(itertools.chain(without_split, *after_split))

print(after_split)
print(splitted_words)
print(without_split)
print(prepared_args)

new_dict: Dict[str,str] = {}
for arg in prepared_args:
    if arg not in inp.keys():
        raise ValueError
    if inp[arg] == "":
        new_dict[arg] = "Empty value"
    else:
        new_dict[arg] = inp[arg]

for i, list_x in enumerate(after_split):
    new_string = ""
    for element in list_x:
        new_string = new_string + " " + inp[element]
    new_dict[splitted_words[i]] = new_string.lstrip()

for to_pop in list(itertools.chain(*after_split)):
    print(to_pop, "dupa")

print(new_dict)