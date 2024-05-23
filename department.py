

class Department:
    def __init__(self, headman_dep, name_department):
        self.name_department = name_department
        self.headman_dep = headman_dep
        self.list_groups = []

    def get_groups(self):
        return self.list_groups

    def get_headman_dep(self):
        return self.headman_dep



    def get_list_group(self):
        return self.list_groups

    def add_group_to_department(self, group):
        return self.list_groups.append(group)

    def get_name_depart(self):
        return self.name_department

    def get_group(self, name_group):
        for i in self.list_groups:
            if name_group == i.get_name_group():
                return i

