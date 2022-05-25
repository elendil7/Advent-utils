from typing import Any, Callable


def string_split_map(string: str, fn: Callable, splitat="\n") -> list:
    temp = string.split(splitat)
    return list(map(fn, temp))


def substring(string: str, first: int, last: int) -> str:
    """gets the substring of the string

    Args:
        string (str): the base string
        first (int): the first index
        last (int): the last index

    Returns:
        str: the substring of string
    """
    return string[first:last]


def get_within_characters(string: str, strl: str, strr: str) -> str:
    """gets the string that is within the characters of the parameters

    Args:
        string (str): the base string
        strl (str): the left character / opening character
        strr (str): the right character / closing character

    Returns:
        str: the string within strl and strr
    """
    firstidx = string.find(strl)
    lastidx = string.rfind(strr)
    return substring(string, firstidx+1, lastidx)


def get_within_parentheses(string: str) -> str:
    return get_within_characters(string, '(', ')')


def get_within_angle_brackets(string: str) -> str:
    return get_within_characters(string, '<', '>')


def get_within_curly_brackets(string: str) -> str:
    return get_within_characters(string, '{', '}')


def get_within_square_brackets(string: str) -> str:
    return get_within_characters(string, '[', ']')


def reverse(string: str) -> str:
    """returns the reverse of the string

    Args:
        string (str): string to reverse

    Raises:
        TypeError: if the input is not a string

    Returns:
        str: the reversed string
    """

    if not is_string(string):
        raise TypeError

    return string[::-1]


def is_string(obj: Any) -> bool:
    """checks if the obj is a str

    Args:
        obj (Any): the object to check  

    Returns:
        bool: if the object is a str or not
    """
    return isinstance(obj, str)


def words(string: str) -> list[str]:
    return string.split(" ")
