"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
lst = ['разработка', 'администрирование', 'protocol', 'standard']
for word in lst:
    word_byte = word.encode('utf-8', 'replace')
    word_decode = word_byte.decode('utf-8')
    print(word, word_byte, word_decode)
