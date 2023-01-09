# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('input.txt', 'r', encoding='utf-8') as in_file:
    lines = in_file.readlines()
    print(f'Строк в файле: {len(lines)}')
    for i, line in enumerate(lines, 1):
        line = line.rstrip().split()
        print(f'Слов в строке {i}: {len(line)}')
