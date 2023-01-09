# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
with open('input.txt', 'r', encoding='utf-8') as in_file:
    sum_salary, count_salary = 0, 0
    for line in in_file.readlines():
        line = line.rstrip().split()
        sum_salary += float(line[1])
        count_salary += 1
        if float(line[1]) < 20000:
            print(line[0])

print(f'Средняя величина дохода сотрудников: {sum_salary / count_salary}')
