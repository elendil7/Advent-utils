from typing import Callable


def string_split_map(string: str, fn: Callable, splitat="\n") -> list:
    temp = string.split(splitat)
    return list(map(fn, temp))
