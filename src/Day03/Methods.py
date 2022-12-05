import string


def calc_scoring_lower(letter: str):
    i = 1
    for c in string.ascii_lowercase:
        if c in letter:
            return i
        else:
            i = i + 1


def calc_scoring_upper(letter: str):
    i = 27
    for c in string.ascii_uppercase:
        if c in letter:
            return i
        else:
            i = i + 1
