#работа со строками

fio = "Романченко Роман Николаевич"
print(type(fio))
print(fio.split(' '))

spleted_fio = fio.split(' ')
surnaem = spleted_fio[0]
name = spleted_fio[1]
middle_name = spleted_fio[2]
print('Фамилия: ' + surnaem + ', имя: ' + name + ', отчество: ' + middle_name + '.')
print(f"Фамилия: {surnaem}, имя: {name}, отчество: {middle_name}.")