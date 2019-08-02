import click
import json
from simulator.attack_simulator import attack_simulator_dict


def battle_list():
    from hero_list.heros import aragon_list, frodo_list
    from hero_list.helpers.list_to_dict import list_to_dict

    aragon = list_to_dict(aragon_list)
    frodo = list_to_dict(frodo_list)

    attack_simulator_dict(aragon)
    attack_simulator_dict(frodo)

    print(json.dumps(aragon))
    print(json.dumps(frodo))


def battle_dict():
    from hero_dict.heros import aragon_dict, frodo_dict

    attack_simulator_dict(aragon_dict)
    attack_simulator_dict(frodo_dict)

    print(json.dumps(aragon_dict))
    print(json.dumps(frodo_dict))


def battle_nt():
    from hero_namedtuple.heros import aragon_nt, frodo_nt

    try:
        attack_simulator_dict(aragon_nt._asdict())
    except TypeError:
        print(aragon_nt._asdict())
        print('\aHmmm.... Something has gone horribly wrong')

    try:
        attack_simulator_dict(frodo_nt._asdict())
    except TypeError:
        print(frodo_nt._asdict()['weapon'])
        print('\aHmmm... Something has gone horribly wrong')

    print(json.dumps(aragon_nt._asdict()))
    print(json.dumps(frodo_nt._asdict()))


def battle_class():
    from hero_class.heros import aragon_class, frodo_class
    aragon = dict(aragon_class)
    frodo = dict(frodo_class)

    attack_simulator_dict(aragon)
    attack_simulator_dict(frodo)

    print(json.dumps(aragon))
    print(json.dumps(frodo))


def battle_dataclass():
    pass


@click.command()
@click.option('--battle', default='list')
def cli(battle):
    battle_map = {
        'list': battle_list, 'dict': battle_dict, 'nt': battle_nt,
        'class': battle_class}
    func = battle_map.get(battle.lower(), 'list')
    func()
