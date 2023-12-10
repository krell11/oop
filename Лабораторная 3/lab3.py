class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f'Книга: {self.name}, автор: {self.author}'

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f"{key}={getattr(self, key)}" for key in self._get_public_attributes()])
        return f"{class_name}({attributes})"

    def _get_public_attributes(self):
        return [a for a in dir(self) if not a.startswith('_') and not callable(getattr(self, a))]


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц может быть только int")
        elif value <= 0:
            raise ValueError("Значиение количества страниц должно быть строго больше нуля")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, {self.pages} страниц."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float|int):
            raise TypeError("Длительность может быть только в формате float|int")
        elif value <= 0:
            raise ValueError("Длительность аудиокниги должна быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, длится: {self.duration}."
