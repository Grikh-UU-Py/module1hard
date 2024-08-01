grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(list(students))#показ множества студентов
students_list=list(students)#преобразование множества в список
print(students_list)#показ списка студентов
res=students_list.sort()#сортировка списка студентов в алфовитном порядке
print(students_list)#показ списка студентов в алфавитном порядке
sr_bal=sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])#подсчёт среднего бала
print(sr_bal)#показ подсчёта среднего бала
journal={students_list[0]:sr_bal[0],students_list[1]:sr_bal[1],students_list[2]:sr_bal[2],students_list[3]:sr_bal[3],students_list[4]:sr_bal[4]}#формирование журнала
print(journal)#показ журнала