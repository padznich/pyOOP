# coding=utf-8

import shelve
from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100)
tom = Manager('Tom Jones', 500)

db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()

