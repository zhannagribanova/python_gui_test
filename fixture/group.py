from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        # group_list = [node.text() for node in root.children()]
        group_list = []
        for node in root.children():
            name = node.text()
            identifier = node.elem
            group_list.append(Group(name=name, identifier=identifier))
        self.close_group_editor()
        return list(group_list)

    def add_new_group(self, group):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(group.name)
        input.type_keys('\n')
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.group_editor = self.app.application.window(title='Group editor')
        self.group_editor.wait('visible')

    def close_group_editor(self):
        self.group_editor.close()

    def select_group_by_index(self, index):
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        root.children()[index].click()
        # self.group_editor.window(runtime_id="42.2820222.4.'%s'" % id).click()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        self.select_group_by_index(index)
        # submit deletion
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_delete = self.app.application.window(title='Delete group')
        self.group_delete.wait('visible')
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()
