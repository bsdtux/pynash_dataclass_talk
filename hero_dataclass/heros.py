from dataclasses import dataclass, field
from typing import List


@dataclass
class HeroDataClass:
    """Class to represent a Council of Elrond Hero"""
    name: str = ''
    species: str = ''
    age: int = 0
    inventory: List = field(default_factory=list)
    weapon: str = ''
    max_dmg: int = 0

    def attack(self):
        print(
            f"{self.name} has used the weapon {self.weapon} to attack a smelly orc!")


if __name__ == '__main__':
    pass
