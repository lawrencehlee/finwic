def strip_extension(filename):
    if filename[0] == '.':
        return filename[1:]
    else:
        return filename.split('.')[0]

def parse_upper_camel_case(word):
    pass

def parse_lower_camel_case(word):
    pass

def parse_snake_case(word):
    return word.split('_')

def parse_kebab_case(word):
    return word.split('-')
