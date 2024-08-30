"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
📌 list-архивы также являются свойствами экземпляра
"""


class Archive:
    numbers_archive = []
    strings_archive = []
    last_num = None
    last_str = None

    def __init__(self, number, string):
        """Инициализирует новый экземпляр Архива."""
        self.number = number
        self.string = string

        if Archive.last_num is not None:
            Archive.numbers_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strings_archive.append(Archive.last_str)

        Archive.last_num = number
        Archive.last_str = string


    def get_archive(self):
        return list(zip(Archive.numbers_archive, Archive.strings_archive))


if __name__ == '__main__':
    a1 = Archive(10, "Привет!")
    a2 = Archive(20, "Как дела?")
    a3 = Archive(30, "Отлично!")
    print(a1.get_archive())
    print(a2.numbers_archive)
    print(a3.strings_archive)