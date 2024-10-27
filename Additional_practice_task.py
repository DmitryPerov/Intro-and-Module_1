from xml.sax.handler import property_interning_dict

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
res = students_list.sort()
count = 0
print('{', end = '')
for i in grades:
    avg = sum(i)/len(i)
    print("'",students_list[count],"':", avg, sep = '', end ='')
    if count < len(grades)-1:
        print(',', sep = '', end='')
    count = count + 1
print('}', end = '')
