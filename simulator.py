import click
from battle_simulator.battle import (battle_list, battle_nt, battle_dict, battle_class, battle_dataclass)
from battle_simulator.json import (json_list, json_nt, json_dict, json_class, json_dataclass)


def banner(simulator_type, data_type):
    letter_count = len(simulator_type) + len(data_type) + 1
    pad_left = (178 - letter_count) // 2
    pad_right = (178 - letter_count) - pad_left
    print()
    print('=' * 180)
    print('=' + ' ' * 178 + '=')
    print('=' + ' ' * pad_left + simulator_type + ':' + data_type + ' ' * pad_right + '=')
    print('=' + ' ' * 178 + '=')
    print('=' * 180)


@click.command()
@click.option('--battle', default='')
@click.option('--json', default='')
def cli(json, battle):
    battle_map = {
        'list': battle_list, 'dict': battle_dict, 'namedtuple': battle_nt,
        'class': battle_class, 'dataclass': battle_dataclass
    }
    json_map = {
        'list': json_list, 'dict': json_dict, 'namedtuple': json_nt,
        'class': json_class, 'dataclass': json_dataclass
    }

    if battle:
        banner('BATTLE', battle)
        func = battle_map.get(battle.lower(), 'list')
        func()
    if json:
        banner('JSON', json)
        func = json_map.get(json.lower(), 'list')
        func()
