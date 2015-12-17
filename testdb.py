# coding=utf-8

import glob
import shelve

print(glob.glob('person*')) # shows all files in the folder

db = shelve.open('persondb')

print('Количество записей в объектк: {}'.format(len(db)))

print('Ключи в объекте: {}'.format(db.keys()))

bob = db['Bob Smith']
print(bob) # Вызов __str__ из AttrDisplay
print('Bob last name is {}'.format(bob.lastName()))

for key in sorted(db):
    print(key, '=>', db[key])