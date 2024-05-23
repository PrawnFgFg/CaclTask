from university import University
from faculty import Faculty
from department import Department
from group import Group
from people import *




ALTGTU = University("ALTGTU")
FIT = Faculty("FIT")
FST = Faculty("FST")

ALTGTU.add_fac_to_university(FIT)
ALTGTU.add_fac_to_university(FST)

ISE = Department("Anna Denisovna", "Information systems in economics")
innovatick = Department("Alik", "Innovation Project Management")

FIT.add_department_to_fac(ISE)
FST.add_department_to_fac(innovatick)


PIE_31 = Group("PIE-31", False, "some...")
PIE_32 = Group("PIE-32", "Loldfdfdffd", "sodfdfdfme...")
IPM_1 = Group("IPM-1", False, "some...")


ISE.add_group_to_department(PIE_31)
ISE.add_group_to_department(PIE_32)
innovatick.add_group_to_department(IPM_1)

student_Den = Student("Den", "Orlov", "Andreevich", 5, 6, 7, 7, "PIE-31")
student_Ura = Student("Ura", "Ivarov", "Sergeevich", 5, 6, 7, "родителей нет", "PIE-31")
student_Anjela = Student("Anjela", "Lipovya", "Antonovna", 5, 6, 7, "родителей нет", "PIE-32")

student_Kira = Student("Kira", "THE BEST", "Ferrari", 4, 4, 4, 4, "IPM-1")
student_Nyrik = Student("Nyrik", "Kish-Mish", "Jordan", 2, 2, 2, 2, "IPM-1")
student_Jopen = Student("Jopen", "Modjery", "Asvoldov", 1, 1, 1, 1, "IPM-1")




parent1 = Parent("Ivan", "Ivanov", "Ivanovich", 2, 2, 2)
parent1.add_child(student_Anjela)

teacher1 = Teacher('Gosha', 'Bisrtiy', 'Omonovich', 'sex', 'data_passport', 'data_home', 'faculty', 'department')
teacher1.add_child(student_Ura)

teacher2 = Teacher('Aloya', 'Vera', 'Expensive', 'sex', 'data_passport', 'data_home', 'FIT', 'department')
teacher2.add_child(student_Nyrik)

t = Teacher("Alex", "Varfolomeev", "Ivanovich",5,6,1,"FIT", "Information systems in economics")

ALTGTU.add_teacher_to_university(teacher1)
ALTGTU.add_teacher_to_university(t)
ALTGTU.add_teacher_to_university(teacher2)

PIE_31.add_student_to_group(student_Den)
PIE_31.add_student_to_group(student_Ura)
PIE_32.add_student_to_group(student_Anjela)

IPM_1.add_student_to_group(student_Kira)
IPM_1.add_student_to_group(student_Nyrik)
IPM_1.add_student_to_group(student_Jopen)
# di = ALTGTU.list_all_student_sort_by("FIO", parents=None)
# for i in di:
#     print(i.first_name)
# print(di)


#
# print(ALTGTU.get_list_teachers("department"))
#
# print(ALTGTU.get_list_of_headman_dep())
#
#
# print(ALTGTU.get_grps_deps_without_headman())
#
#
# parent1.view_children()
#
# ALTGTU.get_list_teachers_with_children()
#
# print(ALTGTU.list_all_student_sort_by("group"))


