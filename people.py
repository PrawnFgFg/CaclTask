class Human:
    def __init__(self, first_name, last_name, surname, sex, data_passport, data_home, children=None):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.sex = sex
        self.data_passport = data_passport
        self.data_home = data_home
        self.children = children if children is not None else []

    def get_child_list(self):
        return self.children

    def get_FIO(self):
        return self.first_name + " " + self.last_name + " " + self.surname

    def add_child(self, child):
        self.children.append(child)


    def view_children(self):
        print(f"У {self.get_FIO()} имеются дети: ")
        for child in self.children:
            print(f"{child.get_FIO()}")

class Student(Human):
    def __init__(self, first_name, last_name, surname, sex, data_passport, data_home, parents, group):
        super().__init__(first_name, last_name, surname, sex, data_passport, data_home)
        self.parents = parents
        self.group = group

    def get_info_parents(self):
        return self.parents

    def get_st_group(self):
        return self.group



    def __str__(self):
        return self.get_FIO_student()


class Teacher(Human):
    def __init__(self, first_name, last_name, surname, sex, data_passport, data_home, faculty, department):
        super().__init__(first_name, last_name, surname, sex, data_passport, data_home)
        self.faculty = faculty
        self.department = department

    def get_fac(self):
        return self.faculty

    def get_depart(self):
        return self.department

class Parent(Human):
    def __init__(self, first_name, last_name, surname, sex, data_passport, data_home):
        super().__init__(first_name, last_name, surname, sex, data_passport, data_home)










