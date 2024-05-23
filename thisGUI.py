from main import *
import tkinter as tk

root = tk.Tk()
root.title("METANIT.COM")
root.geometry("1500x800")
field = tk.Text(root, width=50, height=100, relief="solid", font="Consolas", bg='silver')

def get_list_student_1():

    if perSORTFIO_1.get() == "No" and perSortFac_1.get() == "No" and perSortGroup_1.get() == "No":
        s = ALTGTU.list_all_student_sort_by(None)
        arr11 = []
        count = 0
        for i in s:
            count += 1
            name = i.get_FIO()
            arr11.append(str(count) + " - " + name + "\n")
            # level_text.set(arr)
            for u in reversed(arr11):
                field.insert(0.0, f"{u} \n")
    if perSORTFIO_1.get() == 'Yes':
        s = ALTGTU.list_all_student_sort_by("FIO")
        arr = []
        count = 0
        for i in s:
            count +=1
            name = i.get_FIO()
            arr.append(str(count) + "- " + name + "\n")
        # level_text.set(arr)
        for u in reversed(arr):
            field.insert(0.0, f"{u} \n")

    if perSortFac_1.get() == "Yes":
        s = ALTGTU.list_all_student_sort_by("fac")
        arr2 = []
        count = 0
        for k, v in s.items():
            key = k
            value = v
            for i in value:
                count += 1
                arr2.append(("\n" + str(count) + " - " + key + ": " + i).strip("{"))
        # level_text.set(arr2)
        field.delete(0.0)
        for u in reversed(arr2):
            field.insert(0.0, f"{u} \n")

    if perSortGroup_1.get() == "Yes":
        s = ALTGTU.list_all_student_sort_by("group")
        arr3 = []
        count = 0
        for k, v in s.items():
            key = k
            value = v
            for i in value:
                count += 1
                arr3.append(str(count) + " - " + key + ": " + i + "\n")
        # level_text.set(arr3)
        for u in reversed(arr3):
            field.insert(0.0, f"{u} \n")
def get_list_student_without_parents_2():
    parents = False
    if peSortFio_without_parents_2.get() == "No" and peSortFio_without_parents_2.get() == "No" and perSortGroup_without_parents_2.get() == "No":
        s = ALTGTU.list_all_student_sort_by(None, parents)
        arr = []
        count = 0
        for i in s:
            count += 1
            name = i.get_FIO()
            arr.append(str(count) + " - " + name + "\n")
            # level_text.set(arr)
            for u in reversed(arr):
                field.insert(0.0, f"{u} \n")
            field.insert(0.0, "\n", "---------", '\n')


    if peSortFio_without_parents_2.get() == 'Yes':
        s = ALTGTU.list_all_student_sort_by("FIO", parents)
        arr = []
        count = 0
        for i in s:
            count +=1
            name = i.get_FIO()
            arr.append(str(count) + "- " + name + "\n")
        # level_text.set(arr)
        for u in reversed(arr):
            field.insert(0.0, f"{u} \n")

    if perSortFac_without_parents_2.get() == "Yes":
        s = ALTGTU.list_all_student_sort_by("fac", parents)
        arr2 = []
        count = 0
        for k, v in s.items():
            key = k
            value = v
            for i in value:
                count += 1
                arr2.append(("\n" + str(count) + " - " + key + ": " + i).strip("{"))
        # level_text.set(arr2)
        for u in reversed(arr2):
            field.insert(0.0, f"{u} \n")

    if perSortGroup_without_parents_2.get() == "Yes":
        s = ALTGTU.list_all_student_sort_by("group", parents)
        arr3 = []
        count = 0
        for k, v in s.items():
            key = k
            value = v
            for i in value:
                count += 1
                arr3.append(str(count) + " - " + key + ": " + i + "\n")
        # level_text.set(arr3)
        for u in reversed(arr3):
            field.insert(0.0, f"{u} \n")

def get_arr_teacher():
    if perSortFIO_3.get() == "No" and perSortFac_3.get() == "No" and perSortGroup_3.get() == "No":
        arr_teachers1 = []
        count = 0
        arr = ALTGTU.get_list_teachers()
        for t in arr:
            count += 1
            arr_teachers1.append(str(count) + " - " + t.get_FIO() + "\n")
        # level_text.set(arr_teachers1)
        for u in reversed(arr_teachers1):
            field.insert(0.0, f"{u} \n")

    if perSortFIO_3.get() == "Yes":
        count = 0
        arr_teachers2 = []
        arr = ALTGTU.get_list_teachers("FIO")
        for teacher in arr:
            count += 1
            arr_teachers2.append(str(count) + " - " + teacher.get_FIO() + "\n")
        # level_text.set(arr_teachers2)
        for u in reversed(arr_teachers2):
            field.insert(0.0, f"{u} \n")

    if perSortFac_3.get() == "Yes":
        count = 0
        arr_teachers3 = []
        arr = ALTGTU.get_list_teachers("fac")
        for fac, teacher in arr.items():
            count += 1
            arr_teachers3.append(str(count) + " - " + fac + ": " + str(teacher) + "\n")
        # level_text.set(arr_teachers3)
        for u in reversed(arr_teachers3):
            field.insert(0.0, f"{u} \n")

    if perSortGroup_3.get() == "Yes":
        count = 0
        arr_teachers4 = []
        arr = ALTGTU.get_list_teachers("department")
        for dep, teacher in arr.items():
            count += 1
            arr_teachers4.append(str(count) + " - " + dep + ": " + str(teacher) + "\n")
        # level_text.set(arr_teachers4)
        for u in reversed(arr_teachers4):
            field.insert(0.0, f"{u} \n")


def get_list_headman_of_depart():
    count = 0
    arr = ALTGTU.get_list_of_headman_dep()
    arr_headmanDEP = []
    for h in arr:
        count += 1
        arr_headmanDEP.append(str(count) + " - " + h + "\n")
    # level_text.set(arr_headmanDEP)
    for u in reversed(arr_headmanDEP):
        field.insert(0.0, f"{u} \n")


def get_list_group_without_headman():
    arr = ALTGTU.get_grps_deps_without_headman()
    main_arr = []
    for i in arr:
        main_arr.append(str(i) + "\n")
    # level_text.set(main_arr)
    for u in reversed(main_arr):
        field.insert(0.0, f"{u} \n")



def list_teachers_with_children():
    arr = ALTGTU.get_list_teachers_with_children()
    count = 0
    main_arr = []
    for i in arr:
        main_arr.append(i + "\n")
    # level_text.set(main_arr)
    for u in reversed(main_arr):
        field.insert(0.0, f"{u} \n")


def test7():
    UT = ["" for _ in range(6)]
    for i in UT:
        field.insert(0.0, f"{i} \n")

btn1_get_list_student = tk.Button(root, text="Список всех студентов", font=("Arial", 12, "bold"), bg="#77EEBA",
                 relief=tk.RAISED,
                 bd=5,
                 command=get_list_student_1)
btn2_get_list_without_parents = tk.Button(root, text="Список студентов без родителей", font=("Arial", 12, "bold"),
                                          bg="#77EEBA",
                                          relief=tk.RAISED,
                                          bd=5,
                                          command=get_list_student_without_parents_2
                                          )
btn3_get_list_teachers = tk.Button(root, text="Список преподавателей", font=("Arial", 12, "bold"), bg="#77EEBA",
                                   relief=tk.RAISED,
                                    bd=5,
                                   command=get_arr_teacher
                                   )
btn4_get_list_headman_of_dep = tk.Button(root, text="Список всех заведующих кафедрами", font=("Arial", 12, "bold"), bg="#77EEBA",
                                   relief=tk.RAISED,
                                    bd=5,
                                   command=get_list_headman_of_depart
                                   )

btn5_list_group_without_headman = tk.Button(root, text="Список всех групп без старост и кафедр без заведующих ", font=("Arial", 12, "bold"), bg="#77EEBA",
                                   relief=tk.RAISED,
                                    bd=5,
                                   command=get_list_group_without_headman
                                   )

btn6_list_teachers_with_children = tk.Button(root, text="Список всех преподавателей, имеющих детей – студентов", font=("Arial", 12, "bold"), bg="#77EEBA",
                                   relief=tk.RAISED,
                                    bd=5,
                                   command=list_teachers_with_children
                                   )

btn7_test = tk.Button(root, text="Сделать отступ", font=("Arial", 12, "bold"), bg="#77EEBA",
                                   relief=tk.RAISED,
                                    bd=5,
                                   command=test7
                                   )



perSORTFIO_1 = tk.StringVar()
perSortFac_1 = tk.StringVar()
perSortGroup_1 = tk.StringVar()
perSORTFIO_1.set("No")
perSortFac_1.set("No")
perSortGroup_1.set("No")

peSortFio_without_parents_2 = tk.StringVar()
perSortFac_without_parents_2 = tk.StringVar()
perSortGroup_without_parents_2 = tk.StringVar()
peSortFio_without_parents_2.set("No")
perSortFac_without_parents_2.set("No")
perSortGroup_without_parents_2.set("No")

perSortFIO_3 = tk.StringVar()
perSortFac_3 = tk.StringVar()
perSortGroup_3 = tk.StringVar()
perSortFIO_3.set("No")
perSortFac_3.set("No")
perSortGroup_3.set("No")

flagSortFIO = tk.Checkbutton(root, text="Сортировать по ФИО", font=("Arial", 11, "bold"), variable=perSORTFIO_1,
                             offvalue="No", onvalue="Yes")
flagSortFac = tk.Checkbutton(root, text="Сортировать по факультету", font=("Arial", 11, "bold"), variable=perSortFac_1,
                             offvalue="No", onvalue="Yes")
flagSortGroup = tk.Checkbutton(root, text="Сортировать по группе", font=("Arial", 11, "bold"), variable=perSortGroup_1,
                             offvalue="No", onvalue="Yes")

flagSortFIO_2 = tk.Checkbutton(root, text="Сортировать по ФИО", font=("Arial", 11, "bold"), variable=peSortFio_without_parents_2,
                             offvalue="No", onvalue="Yes")
flagSortFac_2 = tk.Checkbutton(root, text="Сортировать по факультету", font=("Arial", 11, "bold"), variable=perSortFac_without_parents_2,
                             offvalue="No", onvalue="Yes")
flagSortGroup_2 = tk.Checkbutton(root, text="Сортировать по группе", font=("Arial", 11, "bold"), variable=perSortGroup_without_parents_2,
                             offvalue="No", onvalue="Yes")

flagSortFIO_3 = tk.Checkbutton(root, text="Сортировать по ФИО", font=("Arial", 11, "bold"), variable=perSortFIO_3,
                             offvalue="No", onvalue="Yes")
flagSortFac_3 = tk.Checkbutton(root, text="Сортировать по факультету", font=("Arial", 11, "bold"), variable=perSortFac_3,
                             offvalue="No", onvalue="Yes")
flagSortGroup_3 = tk.Checkbutton(root, text="Сортировать по группе", font=("Arial", 11, "bold"), variable=perSortGroup_3,
                             offvalue="No", onvalue="Yes")



btn1_get_list_student.grid(padx=1, pady=1)
btn2_get_list_without_parents.grid(row=0, column=1, padx=1, pady=1)
btn3_get_list_teachers.grid(row=0, column=2, padx=1, pady=1)
btn4_get_list_headman_of_dep.grid(row=0, column=3, padx=1, pady=1)
btn5_list_group_without_headman.grid(row=2, column=3, padx=55, pady=1)
btn6_list_teachers_with_children.grid(row=4, column=3, padx=55, pady=1)
btn7_test.grid(row=5, column=0, padx=15, pady=15)

flagSortFIO.grid(row=1, column=0, ipadx=1, ipady=1, padx=1, pady=1)
flagSortFac.grid(row=2, column=0, ipadx=1, ipady=1, padx=1, pady=1)
flagSortGroup.grid(row=3, column=0, ipadx=1, ipady=1, padx=1, pady=1)

flagSortFIO_2.grid(row=1, column=1, ipadx=1, ipady=1, padx=1, pady=1)
flagSortFac_2.grid(row=2, column=1, ipadx=1, ipady=1, padx=1, pady=1)
flagSortGroup_2.grid(row=3, column=1, ipadx=1, ipady=1, padx=1, pady=1)

flagSortFIO_3.grid(row=1, column=2, ipadx=1, ipady=1, padx=1, pady=1)
flagSortFac_3.grid(row=2, column=2, ipadx=1, ipady=1, padx=1, pady=1)
flagSortGroup_3.grid(row=3, column=2, ipadx=1, ipady=1, padx=1, pady=1)


field.grid(row=7, column=1)

level_text = tk.StringVar()


tk.Label(root, textvariable=level_text, font=("Arial", 12)).grid()



root.mainloop()