import json


def json_list():
    from hero_list.heros import aragon_list, frodo_list
    from hero_list.helpers.list_to_dict import list_to_dict

    aragon = list_to_dict(aragon_list)
    frodo = list_to_dict(frodo_list)

    print()
    print(json.dumps(aragon))
    print()
    print(json.dumps(frodo))
    print()


def json_dict():
    from hero_dict.heros import aragon_dict, frodo_dict

    print()
    print(json.dumps(aragon_dict))
    print()
    print(json.dumps(frodo_dict))
    print()


def json_nt():
    from hero_namedtuple.heros import aragon_nt, frodo_nt

    print()
    print(json.dumps(aragon_nt._asdict()))
    print()
    print(json.dumps(frodo_nt._asdict()))
    print()


def json_class():
    from hero_class.heros import aragon_class, frodo_class
    aragon = dict(aragon_class)
    frodo = dict(frodo_class)

    print()
    print(json.dumps(aragon))
    print()
    print(json.dumps(frodo))
    print()


def json_dataclass():
    from hero_dataclass.heros import aragon_entity, frodo_entity

    print()
    print(aragon_entity.to_json())
    print()
    print(frodo_entity.to_json())
    print()
