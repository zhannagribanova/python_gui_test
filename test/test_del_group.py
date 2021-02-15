from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group(Group(name='Test'))
    old_list = app.groups.get_group_list()
    index = randrange(len(old_list))
    app.groups.delete_group_by_index(index)
    new_list = app.groups.get_group_list()
    old_list[index:index+1] = []
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)
