import click
import json
from dataclasses import asdict
from simulator.attack_simulator import attack_simulator_dict


def battle_list():
    from hero_list.heros import aragon_list, frodo_list
    from hero_list.helpers.list_to_dict import list_to_dict

    aragon = list_to_dict(aragon_list)
    frodo = list_to_dict(frodo_list)

    attack_simulator_dict(aragon)
    print()
    attack_simulator_dict(frodo)


def battle_dict():
    from hero_dict.heros import aragon_dict, frodo_dict

    attack_simulator_dict(aragon_dict)
    print()
    attack_simulator_dict(frodo_dict)


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

    attack_simulator_dict(aragon)
    print()
    attack_simulator_dict(frodo)


def battle_dataclass():
    from hero_dataclass.heros import aragon_entity, frodo_entity

    attack_simulator_dict(asdict(aragon_entity))
    print()
    attack_simulator_dict(asdict(frodo_entity))


def json_list():
    from hero_list.heros import aragon_list, frodo_list
    from hero_list.helpers.list_to_dict import list_to_dict

    aragon = list_to_dict(aragon_list)
    frodo = list_to_dict(frodo_list)

    print(json.dumps(aragon))
    print()
    print(json.dumps(frodo))


def json_dict():
    from hero_dict.heros import aragon_dict, frodo_dict

    print(json.dumps(aragon_dict))
    print()
    print(json.dumps(frodo_dict))


def json_nt():
    from hero_namedtuple.heros import aragon_nt, frodo_nt

    print(json.dumps(aragon_nt._asdict()))
    print()
    print(json.dumps(frodo_nt._asdict()))


def json_class():
    from hero_class.heros import aragon_class, frodo_class
    aragon = dict(aragon_class)
    frodo = dict(frodo_class)

    print(json.dumps(aragon))
    print()
    print(json.dumps(frodo))


def json_dataclass():
    from hero_dataclass.heros import aragon_entity, frodo_entity

    print(aragon_entity.to_json())
    print()
    print(frodo_entity.to_json())


@click.command()
@click.option('--battle', default='')
@click.option('--json', default='')
def cli(json, battle):
    battle_map = {
        'list': battle_list, 'dict': battle_dict, 'nt': battle_nt,
        'class': battle_class, 'dataclass': battle_dataclass
    }
    json_map = {
        'list': json_list, 'dict': json_dict, 'nt': json_nt,
        'class': json_class, 'dataclass': json_dataclass
    }
    if battle:
        func = battle_map.get(battle.lower(), 'list')
        func()
    if json:
        func = json_map.get(json.lower(), 'list')
        func()