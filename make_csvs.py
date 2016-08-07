#!/usr/bin/env python3
import os.path
from xml.etree import ElementTree
from zipfile import ZipFile
from collections import namedtuple
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
from glob import glob

from utils import ensure_dir_exists, iflatten, open_csv_writer


NGData = namedtuple('NGData', 'id level object_names')


def make_csvs(source_dir='zips', target_dir='csvs', pool_size=cpu_count()):
    ensure_dir_exists(target_dir)

    zip_filenames = glob(os.path.join(source_dir, '*.zip'))

    try:
        f1, roots = open_csv_writer(os.path.join(target_dir, 'roots.csv'))
        f2, objects = open_csv_writer(os.path.join(target_dir, 'objects.csv'))

        roots.writerow(('id', 'level'))
        objects.writerow(('id', 'object_name'))

        with ProcessPoolExecutor(pool_size) as executor:
            ngdata_per_zip = executor.map(extract_ngdata_from_zip, zip_filenames)
            for ngdata in iflatten(ngdata_per_zip):
                roots.writerow((ngdata.id, ngdata.level))
                for object_name in ngdata.object_names:
                    objects.writerow((ngdata.id, object_name))
    finally:
        f1.close()
        f2.close()


def extract_ngdata_from_zip(filename):
    return list(map(extract_ngdata_from_xml, iter_xmls_from_zip(filename)))


def iter_xmls_from_zip(filename):
    with ZipFile(filename, 'r') as this_zip:
        for inner_filename in this_zip.namelist():
            if inner_filename.endswith('.xml'):
                xml_string = this_zip.read(inner_filename)
                yield ElementTree.fromstring(xml_string)


def extract_ngdata_from_xml(xml):
    id_ = xml.find('var[@name="id"]').attrib['value']
    level = xml.find('var[@name="level"]').attrib['value']
    objects = [
        obj.attrib['name']
        for obj in xml.findall('objects/object')
    ]
    return NGData(id_, level, objects)


if __name__ == '__main__':
    make_csvs()
