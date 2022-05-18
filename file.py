from typing import Callable, Dict
import itertools
from functools import wraps

def greeter(func):
    def greet(self):
        name: str = func(self)
        name = name.lower()
        name_splitted = name.split()
        fin_list = [x.capitalize() for x in name_splitted]
        res = "Aloha " + ' '.join(fin_list)
        return res
    return greet


def sums_of_str_elements_are_equal(func):
    def wrapper(self):
        inp: str = func(self)
        inp_splitted = inp.split()
        for i, element in enumerate(inp_splitted):
            if "-" in element:
                inp_splitted[i] = [-int(x) for x in element[1:]]
            else:
                inp_splitted[i] = [int(x) for x in element[:]]
        sum_1 = sum(inp_splitted[0])
        sum_2 = sum(inp_splitted[1])
        if sum_1 == sum_2:
            return f"{sum_1} == {sum_2}"
        else:
            return f"{sum_1} != {sum_2}"
    return wrapper


def format_output(*required_keys):
    def decorator(func):
        def wrapper(self):
            inp: Dict[str,str] = func(self)
            splitted_words = []
            after_split = []
            without_split = []
            for key in required_keys:
                if "__" in key:
                    after_split.append(key.split("__"))
                    splitted_words.append(key)
                else:
                    without_split.append(key)
                prepared_args = list(itertools.chain(without_split, *after_split))
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
                if to_pop in new_dict.keys():
                    new_dict.pop(to_pop)

            return new_dict            
        return wrapper
    return decorator


def add_method_to_instance(klass: object):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self):
            return func()
        setattr(klass, func.__name__, wrapper)
        return func
    return decorator

