from src import string_split_map, get_within_parentheses


def test_string_split_map_empty():
    assert string_split_map("", str) == [""]


def test_within_parentheses():
    assert get_within_parentheses("(test)") == "test"
