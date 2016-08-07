import os.path
from random import choice
from string import ascii_letters, digits


RANDOM_STRING_CHARS = ascii_letters + digits


def joining(f):
    def wrapper(*args, **kwargs):
        return ''.join(f(*args, **kwargs))
    return wrapper


def random_string():
    return ''.join(choice(RANDOM_STRING_CHARS) for _ in range(25))


def ensure_dir_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)
