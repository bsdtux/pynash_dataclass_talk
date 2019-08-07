import json
from decimal import Decimal
from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    """Class to represent an Item"""
    name: str = ''
    weight: float = 0.0
    value: Decimal = Decimal(0.00)

    def to_dict(self):
        return {
            'name': self.name,
            'weight': str(self.weight),
            'value': str(Decimal(self.value.quantize(Decimal('.01'))))
        }


@dataclass
class Weapon(Item):
    """Class to represent a weapon"""
    max_dmg: int = 0

    def to_dict(self):
        data = super(Weapon, self).to_dict()
        data['max_dmg'] = self.max_dmg

        return data


@dataclass
class Hero:
    """Class to represent a Council of Elrond Hero"""
    name: str = ''
    species: str = ''
    age: int = 0
    inventory: List[Item] = field(default_factory=list)
    weapon: Weapon = Weapon()

    def to_json(self):
        data = {
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'inventory': [item.to_dict() for item in self.inventory],
            'weapon': self.weapon.to_dict()
        }

        return json.dumps(data)


aragon_entity = Hero(
    name='Aragorn II Elessar', species='Human', age=87,
    inventory=[
        Item(name='Bow', weight=2.1, value=Decimal(10.00)),
        Item(name='arrows', weight=10.00, value=Decimal(20.00))
    ],
    weapon=Weapon(
        name='Andúril', max_dmg=10, weight=5.0, value=Decimal(9999.99)
    )
)

frodo_entity = Hero(
    name='Frodo Baggins', species='Hobbit', age=33,
    inventory=[
        Item(name='The One Ring', weight=1.25, value=Decimal(999999.99)),
        Item(name='Russet Gold Potato', weight=.12, value=Decimal(0.00))
    ],
    weapon=Weapon(name='Sting', max_dmg=5, weight=4.6, value=Decimal(139.99))
)