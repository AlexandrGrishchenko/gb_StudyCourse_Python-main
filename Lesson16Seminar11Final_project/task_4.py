"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
list = ['разработка', 'администрирование', 'protocol', 'standard']
for word in list:
    p = word.encode('utf-8', 'replace')
    word_decode = p.decode('utf-8')
    print(word, p, word_decode)
