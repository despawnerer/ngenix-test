#!/usr/bin/env python3
import os.path
from zipfile import ZipFile
from random import randint
from uuid import uuid4
from multiprocessing import Pool, cpu_count

from utils import joining, ensure_dir_exists, random_string


def make_all_zips(count=50, target_dir='zips', pool_size=cpu_count()):
    ensure_dir_exists(target_dir)
    filenames = [
        os.path.join(target_dir, '%d.zip' % index)
        for index in range(count)
    ]
    with Pool(pool_size) as pool:
        return pool.map(make_zip, filenames)


def make_zip(filename):
    with ZipFile(filename, 'w') as this_zip:
        for n in range(100):
            this_zip.writestr('%s.xml' % n, build_xml())


@joining
def build_xml():
    yield '<root>'
    yield '<var name="id" value="%s"/>' % uuid4()
    yield '<var name="level" value="%d"/>' % randint(1, 100)
    yield '<objects>'
    for _ in range(randint(1, 10)):
        yield '<object name="%s"/>' % random_string()
    yield '</objects>'
    yield '</root>'


if __name__ == '__main__':
    make_all_zips()
