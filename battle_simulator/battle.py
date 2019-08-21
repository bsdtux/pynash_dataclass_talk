from .attack_simulator import attack_simulator_dict
from dataclasses import asdict


def battle_list():
    from hero_list.heros import aragon_list, frodo_list
    from hero_list.helpers.list_to_dict import list_to_dict

    aragon = list_to_dict(aragon_list)
    frodo = list_to_dict(frodo_list)

    print()
    attack_simulator_dict(aragon)
    print()
    attack_simulator_dict(frodo)
    print()


def battle_dict():
    from hero_dict.heros import aragon_dict, frodo_dict

    print()
    attack_simulator_dict(aragon_dict)
    print()
    attack_simulator_dict(frodo_dict)
    print()


def battle_nt():
    from hero_namedtuple.heros import aragon_nt, frodo_nt

    try:
        attack_simulator_dict(aragon_nt._asdict())
    except TypeError:
        print('\aHmmm.... Something has gone horribly wrong')
        print(aragon_nt._asdict())

    print()

    try:
        attack_simulator_dict(frodo_nt._asdict())
    except TypeError:
        print('\aHmmm... Something has gone horribly wrong')
        print(frodo_nt._asdict())


def battle_class():
    from hero_class.heros import aragon_class, frodo_class
    aragon = dict(aragon_class)
    frodo = dict(frodo_class)

    print()
    attack_simulator_dict(aragon)
    print()
    attack_simulator_dict(frodo)
    print()


def battle_dataclass():
    from hero_dataclass.heros import aragon_entity, frodo_entity

    print()
    attack_simulator_dict(asdict(aragon_entity))
    print()
    attack_simulator_dict(asdict(frodo_entity))
    print()
