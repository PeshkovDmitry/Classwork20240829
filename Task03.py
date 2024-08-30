"""
Задание №3
📌 Добавьте к задачам 1 и 2 строки документации для классов.
"""

import time


class MyString(str):
    """Класс, наследующий от str,
    с дополнительными атрибутами автора и времени создания."""

    def __new__(cls, string, author, creation_time=None):
        """Создает новый объект класса MyString."""
        if creation_time is None:
            creation_time = time.time()
        obj = super().__new__(cls, string)
        obj.author = author
        obj.creation_time = creation_time
        return obj

    def __repr__(self):
        """Возвращает строковое представление объекта."""
        return f"MyString('{self}', author='{self.author}', creation_time={self.creation_time})"


class Archive:
    """Класс для хранения пары свойств и сохранения истории."""

    def __init__(self, number, string):
        """Инициализирует новый экземпляр класса Archive."""
        self.number = number
        self.string = string
        if not hasattr(self.__class__, 'numbers_archive'):
            self.__class__.numbers_archive = []
        if not hasattr(self.__class__, 'strings_archive'):
            self.__class__.strings_archive = []
        self.__class__.numbers_archive.append(number)
        self.__class__.strings_archive.append(string)


    def get_archive(self):
        return list(zip(self.__class__.numbers_archive, self.__class__.strings_archive))

if __name__ == '__main__':
    print(Archive.__doc__)
    print(help(Archive))

