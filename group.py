

class Group:

    def __init__(self, number_group, headman, main_department):
        self.number_group = number_group
        self.headman = headman
        self.main_department = main_department
        self.list_students = []

    def get_all_students(self):
        return self.list_students

    def add_student_to_group(self, student):
        if student.get_st_group() != self.number_group:
            raise SyntaxError("Этого студента нельзя добавить в эту группу")
        else:
            self.list_students.append(student)

    def get_name_group(self):
        return self.number_group

    def get_headman(self):
        return self.headman