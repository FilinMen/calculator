#сложение
def add(a):
    for i in range(1, len(list_num)):
        list_num[0] += list_num[i]
    return  list_num[0]
#умножение
def mul(a):
    for i in range(1, len(list_num)):
        list_num[0] *= list_num[i]
    return list_num[0]
#разность 
def sub(a):
    for i in range(1, len(list_num)):
        list_num[0] -= list_num[i]
    return list_num[0] 
#деление
def div(a):
    for i in range(1, len(list_num)):
        list_num[0] /= list_num[i]
    return list_num[0]

print('ВВЕДИТЕ ВАШ ПРИМЕР:')
example = input()
list_num = []
#СТЕПЕНЬ
def mul(a):
    for i in range(1, len(list_num)):
        list_num[0] **= list_num[i]
    return list_num[0]

#СЛОЖЕНИЕ
if '+' in example:
    print('addition')
    example.replace(' ', '') #УДАЛЕНИЕ ПРОБЕЛОВ
    spl_ex = example.split('+')# РАЗДЕЛЕНИЕ ПО ЗНАКУ
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = add(list_num)
#УМНОЖИТЬ
elif '*' in example:
    print('multiply')
    example.replace(' ', '')
    spl_ex = example.split('*')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = mul(list_num)
#РАЗНОСТЬ
elif '-' in example:
    print('subtract')
    spl_ex = example.split('-')
    example.replace(' ', '')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    print(list_num[1])
    result = sub(list_num)
#ДЕЛИТЬ
elif '/' in example:
    print('subtract')
    spl_ex = example.split('/')
    example.replace(' ', '')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = div(list_num)
#СТЕПЕНЬ

elif '**' or '^' in example:
    print('degree')
    spl_ex = example.split('**')
    spl_ex = example.split('^')
    example.replace(' ', '')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = div(list_num)
print(result)
