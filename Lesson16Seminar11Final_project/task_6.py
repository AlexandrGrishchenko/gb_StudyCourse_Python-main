"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""
#
import locale
import chardet

# кодировка по умолчанию
def_cod = locale.getpreferredencoding()
print(f"Кодировка по умолчанию:  {def_cod}")

file_txt = open('test_file.txt', 'r')
file_txt.close()
# выдает <_io.TextIOWrapper name='test_file.txt' mode='r' encoding='cp1251'>
print(file_txt)

print()

with open('test_file.txt', 'rb') as in_file:
    for el_str in in_file:
        el_str_bytes = chardet.detect(el_str)
        el_str_utf = el_str.decode(el_str_bytes['encoding']).encode('utf-8')
        print(type(el_str_utf))
        print(el_str_utf)
        print(el_str_utf.decode('utf-8'))


# Второй вариант решения задачи
"""
Создаем текстовый файл под названием "test_file.txt " вручную и заполняем его следующими тремя строками: "сетевое программирование", "сокет", "декоратор".
Используя следующий код, чтобы открыть файл в формате Unicode и распечатываем его содержимое:
Убедившись, что файл может быть открыт и прочитан кем угодно, независимо от кодировки по умолчанию, используемой для записи файла. Чтобы сделать это, нам может потребоваться преобразовать содержимое файла в utf-8 перед его чтением.
Примечание: Режим "rb" используется для открытия файла в двоичном режиме, что необходимо для преобразования содержимого файла в другую кодировку."""
with open("test_file.txt", "rb") as file:
    content = file.read()
    content = content.decode("utf-8")
    print(content)
