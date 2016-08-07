import os.path
import csv
from random import choice
from itertools import chain
from string import ascii_letters, digits


RANDOM_STRING_CHARS = ascii_letters + digits


iflatten = chain.from_iterable


def joining(f):
    def wrapper(*args, **kwargs):
        return ''.join(f(*args, **kwargs))
    return wrapper


def random_string():
    return ''.join(choice(RANDOM_STRING_CHARS) for _ in range(25))


def ensure_dir_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def open_csv_writer(filename):
    file = open(filename, 'w')
    writer = csv.writer(file)
    return file, writer
