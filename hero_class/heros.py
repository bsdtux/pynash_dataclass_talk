from decimal import Decimal, getcontext


class HeroClass:
    def __init__(self, name: str, species, age, inventory, weapon):
        self.name = name
        self.species = species
        self.age = age
        self.inventory = inventory
        self.weapon = weapon

    def __repr__(self):
        str(self)

    def __str__(self):
        return (f'HeroClass - {self.name}, {self.species}, {self.age}, '
                f'{self.inventory}, {self.weapon}')

    def __iter__(self):
        yield 'name', self.name
        yield 'species', self.species
        yield 'age', self.age
        yield 'inventory', [dict(item) for item in self.inventory]
        yield 'weapon', dict(self.weapon)


class Item:
    """Class to represent an Item"""
    def __init__(self, name: str = '', weight: float = 0.0,
                 value: Decimal = Decimal('0.00')):
        self.name = name
        self.weight = weight
        self.value = Decimal(value.quantize(Decimal('.01')))

    def __iter__(self):
        yield 'name', self.name
        yield 'weight', str(self.weight)
        yield 'value', str(self.value)


class Weapon(Item):
    """Class to represent a weapon"""
    def __init__(self, name: str = '', weight: float = 0.0,
                 value: Decimal = Decimal('0.00'), max_dmg: int = 0):
        self.max_dmg = max_dmg
        super().__init__(name=name, weight=weight, value=value)

    def __iter__(self):
        yield 'name', self.name
        yield 'weight', str(self.weight)
        yield 'value', str(self.value)
        yield 'max_dmg', self.max_dmg


aragon_class = HeroClass(
    name='Aragorn II Elessar', species='Human', age=87,
    inventory=[
        Item(name='Bow', weight=2.1, value=Decimal(10.00)),
        Item(name='arrows', weight=10.00, value=Decimal(20.00))
    ],
    weapon=Weapon(
        name='Andúril', max_dmg=10, weight=5.0, value=Decimal(9999.99)
    )
)

frodo_class = HeroClass(
    name='Frodo Baggins', species='Hobbit', age=33,
    inventory=[
        Item(name='The One Ring', weight=1.25, value=Decimal(999999.99)),
        Item(name='Russet Gold Potato', weight=.12, value=Decimal(0.00))
    ],
    weapon=Weapon(name='Sting', max_dmg=5, weight=4.6, value=Decimal(139.99))
)
