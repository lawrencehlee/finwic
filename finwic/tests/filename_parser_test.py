from finwic.filename_parser import *

def strip_extension_test():
    filename = "bob.html.erb"
    assert strip_extension(filename) == "bob"
    filename = ".config"
    assert strip_extension(filename) == "config"

def parse_upper_camel_case_test():
    word = "GoneWithTheWind"
    assert parse_upper_camel_case(word) == ["gone", "with", "the", "wind"]
    word = "ABigMistake"
    assert parse_upper_camel_case(word) == ["a","big", "mistake"]
    word = "IncorrectHTTPString"
    assert parse_upper_camel_case(word) == ["incorrect", "http", "string"]

def parse_lower_camel_cass_test():
    word = "goneWithTheWind"
    assert parse_lower_camel_case(word) == ["gone", "with", "the", "wind"]
    word = "httpYonderBo"
    assert parse_lower_camel_case(word) == ["http", "yonder", "bo"]
    word = "incorrectHTTPString"
    assert parse_lower_camel_case(word) == ["incorrect", "http", "string"]
    word = "bob"
    assert parse_lower_camel_case(word) == ["bob"]

def parse_snake_case_test():
    word = "anyways"
    assert parse_snake_case(word) == ["anyways"]
    word = "little_Bobby_TABLES"
    assert parse_snake_case(word) == ["little", "bobby", "tables"]

def parse_kebab_case_test():
    word = "anyways"
    assert parse_snake_case(word) == ["anyways"]
    word = "little-Bobby_TABLES-no"
    assert parse_snake_case(word) == ["little", "bobby_tables", "no"]
