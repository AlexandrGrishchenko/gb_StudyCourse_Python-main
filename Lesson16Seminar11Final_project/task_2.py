"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
# Первый вариант
str1 = b'class'
str2 = b'function'
str3 = b'method'
print(type(str1), type(str2), type(str3))
print(str1, str2, str3)
print(len(str1), len(str2), len(str3))
print('\n')

# Второй вариант
lst = [b'class', b'function', b'method']

for line in lst:
    print('тип переменной: {}'.format(type(line)))
    print('содержание переменной - {}'.format(line))
    print('длинна строки: {}'.format(len(line)))
    print()
