from src import string_split_map


def test_string_split_map_empty():
    assert string_split_map("", str) == [""]
