
class Faculty:
    def __init__(self, name_fac):
        self.name_fac = name_fac
        self.list_departments = []

    def get_list_dep(self):
        return self.list_departments


    def add_department_to_fac(self, department):
        return self.list_departments.append(department)

    def get_name_fac(self):
        return self.name_fac

    def get_department(self, name_depart):
        for i in self.list_departments:
            if name_depart == i.get_name_depart():
                return i