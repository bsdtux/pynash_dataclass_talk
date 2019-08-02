from collections import namedtuple

Weapon = namedtuple('Weapon', ['name', 'max_dmg'])
Hero = namedtuple(
    'Hero', ['name', 'species', 'age', 'inventory', 'weapon'])

aragon_nt = Hero(
    name='Aragorn II Elessar', species='Human', age=87,
    inventory=['1 Bow', '10 Some Arrows', '10 gold'],
    weapon=Weapon(name='Andúril', max_dmg=10))

frodo_nt = Hero(
    name='Frodo Baggins', species='Hobbit', age=33,
    inventory=['1 gold potatoe'], weapon=Weapon(name='Sting', max_dmg=5))

