#сложение
def add(a,b):
    return a + b
#умножение
def mul(a,b):
    return a * b
#разность 
def min(a,b):
    return a - b
#деление
def div(a,b):
    return a / b

print('ВВЕДИТЕ ВАШ ПРИМЕР:')
example = input()

if '+' in example:
    print('addition')#сложение
    example.replace(' ', '') #УДАЛЕНИЕ ПРОБЕЛОВ
    spl_ex = example.split('+')# РАЗДЕЛЕНИЕ ПО ЗНАКУ
    list_ex = spl_ex
    first_num = int(list_ex[0])
    another_num = int(list_ex[1])
    v = '+'
elif '*' in example:
    print('multiplication')#умножение
    example.replace(' ', '')
    spl_ex = example.split('*')
    list_ex = spl_ex
    first_num = int(list_ex[0])
    another_num = int(list_ex[1])
    v = '*'
elif '-' in example:
    print('minus')#минус
    spl_ex = example.split('-')
    example.replace(' ', '')
    list_ex = spl_ex
    first_num = int(list_ex[0])
    another_num = int(list_ex[1])
    v = '-'
elif '/' in example:
    print('division')#деление
    spl_ex = example.split('/')
    example.replace(' ', '')
    list_ex = spl_ex
    first_num = int(list_ex[0])
    another_num = int(list_ex[1])
    v = '/'

if v == '+':
    result = add(first_num,another_num)
elif  v == '*':      
    result = mul(first_num,another_num)  
elif v == '-' :   
    result = min(first_num,another_num)
elif v == '/':
    result = div(first_num,another_num)
print(result)

