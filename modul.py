import random
boysnames = ['Роман','Инокентий','Александр','Андрей','Юрий','Максим','Петр', 'Прохор']
boyssurenames = ['Сидоров','Иванов','Петров','Достоевский','Солженицын','Кретов','Малеев']
girlsnames = ['Юлия','Дарья','Ева','Кристина','Виктория','Софья','Анна', 'Ольга']
girlssurenames  = ['Сидорова','Иванова','Петрова','Достоевская','Солженицына','Кретова','Малеева']
subjlist = ['русский язык', 'литература', 'математика', 'иностранный язык', 'история', 'физическая культура', 'музыка', 'технология']
def checkintinput(output,error):
    message = input(output)
    if not message.isdigit():
        print(error)
        return checkintinput(output,error)
    return int(message)


studentdict = {}  

def idfinder():
    arr = list(studentdict.keys())
    id = len(arr)+1 
    return id

# Добавление нового студента (Поля - имя, фамилия)
def addstudent():
    name,surname = input('Введите имя и фамилию ученика(через пробел)').split()
    studentdict.update({f'{name} {surname}':[ (elem,[]) for elem in subjlist]})
   
# Добавление предмета (добавляется всем ученикам сразу)
def addsubject():
    subj = input('Введите название предмета: ')
    for i in studentdict:
        studentdict.get(i).append((subj,[]))

 

#вывод списка учеников
def showstudents():
    studentlist = []
    for i in range(len(studentdict)):
        print(f'{i+1} {list(studentdict.keys())[i]}')
        studentlist.append(list(studentdict.keys())[i])
    return studentlist

# вывод списка предметов
def showsubj():
    i = 1
    for subj in subjlist:
        print(f'{i} {subj}')
        i+=1

def subjgenerator():
    
    for i in studentdict:
        print(subjlist)
        studentdict.get(i).append((subjlist[random.randint(0,7)],[]))


def namegenerator():
    for i in range(50):
        studentdict.update({f'{girlsnames[random.randint(0,6)]} {girlssurenames[random.randint(0,6)]}':[ (elem,[]) for elem in subjlist]})
    for i in range(50):
        studentdict.update({f'{boysnames[random.randint(0,6)]} {boyssurenames[random.randint(0,6)]}':[ (elem,[]) for elem in subjlist]})

# Добавление оценки ученику по предмету (выбираем ученика(из существующих), 
# выбираем предмет(из сущ.),пишем оценку )

marklist  = []
def mark():
    a = showstudents()
    pickstudent = checkintinput('Выберите ученика по номеру в первом столбике: ', 'Некорректный ввод, введите номер ученика!')
    
    if pickstudent > len(studentdict) or pickstudent <= 0:
        print('Некорректный ввод, введите номер ученика!')
        return mark()
    print('\n')
    showsubj()
    picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    while  picksubj > len(subjlist) or picksubj <= 0:
        print('Некорректный ввод, введите номер предмета!')
        showsubj()
        picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    number = checkintinput('Введите оценку : ', 'Некорректный ввод, введите оценку(целое число)!')
    while  number > 5 or number <= 0:
        print('Некорректный ввод, введите оценку(от 1 до 5)!')
        number = checkintinput('Введите оценку : ', 'Некорректный ввод, введите оценку(целое число)!')
    f = studentdict.get(a[pickstudent-1])
    f[picksubj-1][1].append(number)   

def markgenerator():
    for i in studentdict:
        studentdict.get(i)[random.randint(0,7)][1].append(random.randint(1,5))
        




def showmarks():
    a = showstudents()
    pickstudent = checkintinput('Выберите ученика по номеру в первом столбике: ', 'Некорректный ввод, введите номер ученика!')
    
    if pickstudent > len(studentdict) or pickstudent <= 0:
        print('Некорректный ввод, введите номер ученика!')
        return showmarks()
    print(list(studentdict.keys())[pickstudent-1])
    marks = studentdict.get(a[pickstudent-1])
    for mark in marks:
        print(f'{mark[0]} {mark[1]}')

# Вывод средней оценки ученика по одному предмету
def avgmark():
    a = showstudents()
    pick = checkintinput('Выберите ученика','Некорректный ввод!')
    showsubj()
    picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    while  picksubj > len(subjlist) or picksubj <= 0:
        print('Некорректный ввод, введите номер предмета!')
        showsubj()
        picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    f = studentdict.get(a[pick-1])
    avg  = 0
    for elem in f[picksubj-1][1]:
        avg += elem
    avg = round(avg / len(f[picksubj-1][1]),2)  
    print(f'Средняя ценка ученика {list(studentdict.keys())[pick-1]} по {subjlist[picksubj-1]}: {avg}')

# Вывод среднего балла по школе по конкретному предмету
def globalavg():
    picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    while  picksubj > len(subjlist) or picksubj <= 0:
        print('Некорректный ввод, введите номер предмета!')
        showsubj()
        picksubj = checkintinput('Выберите предмет по номеру в первом столбике: ', 'Некорректный ввод, введите номер предмета!')
    avg = 0
    count = 0
    for i in studentdict:
        f = studentdict.get(i)[picksubj-1][1]
        for j in f:
            avg+=j
            count+=1
        
    avg = round(avg / count,2)  
    print(f'Средняя оценка по школе по предмету  {subjlist[picksubj-1]}: {avg}')


# 4)Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
def goldmedal():
    golder = 0
    
    for i in studentdict: 
        count = 0
        nomarks = 0
        f = studentdict.get(i)
        for j in f:
            for k in j[1]:
                print(k)
                if k < 4:
                    count = 0 
                    break
                count = 1
            if len(j[1]) == 0:
                count = 1
            if len(j[1]) > 0:
                nomarks += 1 
            if count == 0:
               break
            
        if count == 1 and nomarks > 0:
            golder += 1
           
    print(f'Кол-во учеников претендующих на золотую медаль:  {golder}')
#добавление в файл

def importer():
    file = open('student.txt', 'w', encoding='utf-8')
    for key, value in studentdict.items():
       file.write(f'{key}, {value}\n')
    file.close()