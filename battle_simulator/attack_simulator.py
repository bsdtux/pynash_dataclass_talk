from random import randrange


def attack_simulator_dict(hero):
    num_attacks = 0
    smelly_orc = {
        'name': 'One smelly orc :)',
        'health': 35
    }

    while smelly_orc['health'] > 1:
        smelly_orc['health'] -= randrange(1, hero['weapon']['max_dmg'])
        num_attacks += 1

    attack_string = 'attacks'

    if num_attacks == 1:
        attack_string = 'attack'

    print(f"Good Job {hero['name']} "
          f"Using your trusted {hero['weapon']['name']} "
          f"You defeated {smelly_orc['name']} "
          f"in {num_attacks} {attack_string}")
