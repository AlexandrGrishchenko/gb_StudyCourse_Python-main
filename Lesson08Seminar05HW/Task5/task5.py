# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
nums = input('Введите числа через пробел: ')

with open('input.txt', 'w', encoding='utf-8') as in_file:
    in_file.writelines(nums)

with open('input.txt', 'r', encoding='utf-8') as in_file:
    print(sum(list(map(int, in_file.readline().split()))))
