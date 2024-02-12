import doctest
import datetime


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """
        :param title: Название книги
        :param author: ФИО автора книги
        :param year: Год выпуска книги

        Пример:
        >>> book = Book(title = "Война и мир", author="Лев Николаевич Толстой", year = 1867)
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f"{self.title} by {self.author}, {self.year}"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление объекта."""
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def get_age(self) -> int:
        """Возвращает возраст книги в годах."""
        current_year = datetime.datetime.now().year
        return current_year - self.year


class FictionBook(Book):
    """Класс, представляющий художественную литературу."""

    def __init__(self, title: str, author: str, year: int, genre: str) -> None:
        """
        Инициализирует новый экземпляр художественной книги с добавлением жанра.
        :param title: Название книги
        :param author: ФИО автора книги
        :param year: Год выпуска книги
        :param genre: Жанр Литературного произведения

        Пример:
        >>> new_book  = FictionBook(title = "Война и мир", author="Лев Николаевич Толстой", year = 1867, genre="Историческая проза" )
        """
        super().__init__(title, author, year)
        self.genre = genre

    def __str__(self) -> str:
        """Возвращает строковое представление художественной книги с информацией о жанре."""
        return super().__str__() + f" Genre: {self.genre}"

    def get_age(self) -> str:
        """Возвращает возраст книги с учетом жанра."""
        age = super().get_age()
        return f"{self.title} is {age} years old and belongs to the {self.genre} genre."


class LearningBook(Book):
    """
    Класс, представляющий учебную литературу.
    :param title: Название книги
    :param author: ФИО автора книги
    :param year: Год выпуска книги
    :param subject: предмет изучения
    Пример:
        >>> new_book  = LearningBook(title = "Математический анализ первая часть", author="Анатолий Петрович Аксенов", year = 1999, subject = "Математика")
    """

    def __init__(self, title: str, author: str, year: int, subject: str) -> None:
        """Инициализирует новый экземпляр нехудожественной книги с добавлением предмета."""
        super().__init__(title, author, year)
        self.subject = subject

    def __str__(self) -> str:
        """Возвращает строковое представление нехудожественной книги с информацией о предмете."""
        return super().__str__() + f" Subject: {self.subject}"


if __name__ == "__main__":
    doctest.testmod()
