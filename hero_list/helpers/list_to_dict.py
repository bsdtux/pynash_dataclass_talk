def list_to_dict(hero: list):
    return {
        'name': hero[0],
        'species': hero[1],
        'age': hero[2],
        'inventory': hero[3],
        'weapon': {
            'name': hero[4],
            'max_dmg': hero[5]
        }
    }
