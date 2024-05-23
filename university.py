
class University:
    def __init__(self, name_university):
        self.name_university = name_university
        self.list_faculties = []
        self.list_teachers = []

    def add_teacher_to_university(self, teacher):
        return self.list_teachers.append(teacher)


    def get_list_teachers(self, param_of_sort=None):
        if param_of_sort == None:
            return self.list_teachers

        elif param_of_sort == "FIO":
            arr = self.list_teachers[:]
            return sorted(arr, key=lambda x: x.get_FIO())

        elif param_of_sort == "fac":
            sort_list_fac = sorted(self.list_faculties, key= lambda x: x.get_name_fac())
            facs_and_teachers = {}
            for f in sort_list_fac:
                arr_teachers = []
                for t in self.list_teachers:
                    if f.get_name_fac() == t.get_fac():
                        arr_teachers.append(t.get_FIO())
                facs_and_teachers[f.get_name_fac()] = arr_teachers
            return facs_and_teachers

        elif param_of_sort == "department":
            departs = [d for f in self.list_faculties for d in f.get_list_dep()]
            sorted_dep = sorted(departs, key=lambda x: x.get_name_depart())
            di_caf_tchrs = {}
            for d in sorted_dep:
                arr_tchrs = []
                for t in self.list_teachers:
                    if d.get_name_depart() == t.get_depart():
                        arr_tchrs.append(t.get_FIO())
                di_caf_tchrs[d.get_name_depart()] = arr_tchrs
            return di_caf_tchrs



    def get_list_facs(self):
        return self.list_faculties


    def get_list_all_students(self):
        arr = []
        for i in self.get_list_facs():
            for j in i.get_list_dep():
                for g in j.get_groups():
                    for student in g.get_all_students():
                        arr.append(student)
        return arr

    def get_list_all_students_without_parents(self):
        arr = []
        for i in self.get_list_facs():
            for j in i.get_list_dep():
                for g in j.get_groups():
                    for student in g.get_all_students():
                        if student.get_info_parents() == "родителей нет":
                            arr.append(student)
        return arr

    def list_all_student_sort_by(self, param_of_sort, parents=None):
        if parents == None:
            arr = self.get_list_all_students()
        else:
            arr = self.get_list_all_students_without_parents()
        if param_of_sort == None:
            return arr
        if param_of_sort == "FIO":
            main_arr = sorted(arr, key=lambda x: x.get_FIO())
            return main_arr
        elif param_of_sort == "fac":
            sorted_facs = sorted(self.get_list_facs(), key=lambda x: x.get_name_fac())
            d = {}
            dg = {}
            for f in sorted_facs:
                list_st = []
                list_st_wp = []
                for j in f.get_list_dep():
                    for g in j.get_groups():
                        for student in g.get_all_students():
                            if student.get_info_parents() == "родителей нет" and parents != None:
                                list_st_wp.append(student.get_FIO())
                            list_st.append(student.get_FIO())

                dg[f.get_name_fac()] = list_st_wp
                d[f.get_name_fac()] = list_st
            if parents != None:
                return dg
            else:
                return d
        elif param_of_sort == "group":
            groups = []
            sorted_gr_st = {}
            sorted_gr_st_wp = {}
            for i in self.get_list_facs():
                for j in i.get_list_dep():
                    for g in j.get_groups():
                        groups.append(g)
            sort_groups = sorted(groups, key=lambda x: x.get_name_group())
            for g in sort_groups:
                stud = []
                stud_wp = []
                for st in g.get_all_students():
                    if st.get_info_parents() == "родителей нет" and parents != None:
                        stud_wp.append(st.get_FIO())
                    stud.append(st.get_FIO())
                sorted_gr_st_wp[g.get_name_group()] = stud_wp
                sorted_gr_st[g.get_name_group()] = stud
            if parents != None:
                return sorted_gr_st_wp
            else:
                return sorted_gr_st


    def add_fac_to_university(self, fac):
        return self.list_faculties.append(fac)

    def get_faculty(self, fac):
        for i in self.list_faculties:
            if fac == i.get_name_fac():
                return i

    def get_list_of_headman_dep(self):
        need_arr = [d.get_headman_dep() for f in self.list_faculties for d in f.get_list_dep()]
        return need_arr


    def get_grps_deps_without_headman(self):
        di = {}
        di2 = {}
        main_arr = []
        arr_groups_without_headman = list(filter(lambda x: x != None, [g.get_name_group() if g.get_headman() == False else None for f in self.list_faculties for d in f.get_list_dep() for g in d.get_groups()]))
        arr_deps_without_headman = list(filter(lambda x : x != None, [d.get_name_depart() if d.get_headman_dep() == False else None for f in self.list_faculties for d in f.get_list_dep()]))
        di["Группы без старост"] = arr_groups_without_headman
        di2["Кафедры без заведующих"] = arr_deps_without_headman
        main_arr.append(di)
        main_arr.append(di2)
        return main_arr

    def get_list_teachers_with_children(self):
        main_arr = []
        for t in self.list_teachers:
            if len(t.get_child_list()) != 0:
                main_arr.append(f'Преподаватель {str(t.get_FIO())} имеет следующих детей: {str([i.get_FIO() for i in t.get_child_list()])}')
        return main_arr