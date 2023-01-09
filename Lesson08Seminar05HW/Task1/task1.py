# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
def get_lines(line):
    lst = []
    while line != '':
        lst += [line + '\n']
        line = input('Ввод: ')
    return lst


lst = get_lines(input('Ввод: '))

with open('output.txt', 'w', encoding='utf-8') as out_file:
    out_file.writelines(lst)
