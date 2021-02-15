from model.group import Group
from random import randint


def test_add_group(app):
    old_list = app.groups.get_group_list()
    new_group = Group(name="my group"+str(randint(1, 100000)))
    app.groups.add_new_group(new_group)
    new_list = app.groups.get_group_list()
    old_list.append(new_group)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)
