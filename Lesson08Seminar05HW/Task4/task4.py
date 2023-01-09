# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_dic = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

in_file = open('input.txt', 'r', encoding='utf-8')
out_file = open('output.txt', 'w', encoding='utf-8')

lines = in_file.readlines()
for line in lines:
    line = line.rstrip().split()
    print(' '.join([num_dic[line[2]]] + line[1:]), file=out_file)

in_file.close()
out_file.close()
