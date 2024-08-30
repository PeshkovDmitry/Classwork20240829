"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time


class MyString(str):

    def __new__(cls, string, author, creation_time=None):
        if creation_time is None:
            creation_time = time.time()
        obj = super().__new__(cls, string)
        obj.author = author
        obj.creation_time = creation_time
        return obj

    def __str__(self):
        return '{0} {1} {2}'

    def __repr__(self):
        return f"MyString('{self}', author='{self.author}', creation_time={self.creation_time})"


if __name__ == '__main__':
    my_str = MyString("Это моя строка!", "Иван Иванов")
    print(my_str.__repr__())
    print(len(my_str))
    print(my_str.upper())
    print(my_str.title())
    print(f'{my_str=}')
