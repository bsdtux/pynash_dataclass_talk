from decimal import Decimal
from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    """Class to represent an Item"""
    name: str = ''
    weight: float = 0.0
    value: Decimal = 0.00


@dataclass
class Weapon(Item):
    """Class to represent a weapon"""
    max_dmg: int = 0


@dataclass
class Inventory:
    """Class to represent a Hero's Inventory"""
    pouch: List[Item] = field(default_factory=list)


@dataclass
class HeroEntitiy:
    """Class to represent a Council of Elrond Hero"""
    name: str = ''
    species: str = ''
    age: int = 0
    inventory: Inventory = field(default_factory=Inventory)
    weapon: Weapon = Weapon()

    def attack(self):
        print(
            f"{self.name} has used their {self.weapon.weight} weapon {self.weapon.name} to attack a smelly orc! dealing {self.weapon.dmg}")

    def show_inventory(self):
        for item in self.inventory.pouch:
            print(item)

if __name__ == '__main__':
    pass