import doctest


class UniversityOnMap:
    def __init__(self, name: str, location: tuple, working_hours: tuple, number_of_students: int):
        """
        Создание и подготовка к работе объекта "Университет"

        :param name: Название университета
        :param location: Локация универститета (Широта, Долгота)
        :param working_hours: Время работы универститета
        :param number_of_students: Количество обучающихся в университете

        Примеры:
        >>> university = UniversityOnMap(name="SPBPU",location=(60.007677, 30.372386), working_hours=(09.00,18.00), number_of_students=32929) #создаение экземпляра класса UniversityOnMap
        """
        if not isinstance(name, str):
            raise TypeError("Название универститета должно передаватсья в формате str")
        self.name = name

        if not isinstance(location, tuple):
            raise TypeError("Локация университета должна передаваться в формате tuple")
        if len(location) != 2 or type(location[0]) != float or type(location[1]) != float:
            raise ValueError("Геолокация должна передаваться в формате (Latitude: float, Longitude: float)")
        if location[0] > 90 or location[0] < -90:
            raise ValueError("Координата широта может находиться в диапазоне [-90, 90]")
        if location[1] > 180 or location[1] < -180:
            raise ValueError("Координата долготы может находиться в диапазоне [-180, 180]")
        self.location = location

        if not isinstance(working_hours, tuple):
            raise TypeError("Рабочее время университета должно передаваться в формате tuple")
        if len(working_hours) != 2:
            raise ValueError("Время работы должно быть указано в формате(start_time, end_time)")
        if any(working_hours) < 0:
            raise ValueError("Время не может быть отрицательным")
        self.working_hours = working_hours

        if not isinstance(number_of_students, int):
            raise TypeError("Количество обучающихся студентов должно передаваться в формате int")
        if number_of_students < 0:
            raise ValueError("Количество студентов не может быть отрицательным")
        self.number_of_students = number_of_students


    def is_working(self, time_: float) -> bool:
        """
        Функция для проверки  работы университета в заданный момент времени
        :param time_: Время для провекри
        :return: Работает ли университет в заданный time_

        Примеры:
        >>> university = UniversityOnMap(name="SPBPU",location=(60.007677, 30.372386), working_hours=(09.00,18.00), number_of_students=32929)
        >>> university.is_working(10)
        """
        if not isinstance(time_, float|int):
            raise TypeError("Время может быть только в формате float|int")
        if time_ < 0:
            raise ValueError("Время не может быть отрицательным")
        ...

    def enroll_students(self, new_students: int) -> None:
        """
        Функция для зачисления новых студентов.
        :param new_students: количество зачисленных студентов

        Примеры:

        >>> university = UniversityOnMap(name="SPBPU",location=(60.007677, 30.372386), working_hours=(09.00,18.00), number_of_students=32929)
        >>> university.enroll_students(1000)
        """
        if not isinstance(new_students, int):
            raise TypeError("Новые студенты могут быть только в формате int")
        if new_students < 0:
            raise ValueError("Количество новых студентов не может быть отрицательным")
        ...

    def expel_students(self, students_to_expel: int) -> None:
        """
        Функция для отчисления студентов.
        :param students_to_expel: количество отчисленных студентов

        Примеры:
        >>> university = UniversityOnMap(name="SPBPU",location=(60.007677, 30.372386), working_hours=(09.00,18.00), number_of_students=32929)
        >>> university.expel_students(1000)
        """
        if not isinstance(students_to_expel, int):
            raise TypeError("Студенты могут быть только в формате int")
        if students_to_expel < 0:
            raise ValueError("Количество студентов не может быть отрицательным")
        ...


class Student:
    def __init__(self, full_name: [str, str, str], stud_id: int, group: int, **description):
        """
        Создание и подготовка к работе объекта "Студент"
        :param full_name: ФИО студента
        :param stud_id: номер студента в системе
        :param group: номер образовательной группы

        Примеры:
        >>> student = Student(full_name=['Иванов','Иван','Иванович'],stud_id=1, group=10, sports=["Футбол","Баскетбол"], favorite_subject="history")

        """

        if not isinstance(full_name, list):
            raise TypeError("ФИО студента должно быть в формате [str,str,str]")
        if len(full_name) < 3:
            raise ValueError("ФИО должно иметь 3 атрибута, даже если нет отчества в full_name должна передаваться пустая "
                             "строка")
        if not all(isinstance(name, str) for name in full_name):
            raise TypeError("Фамилия, Имя и Отчество должны быть записаны в формате str")
        self.full_name = full_name

        if not isinstance(stud_id, int):
            raise TypeError("Номер студента может быть только в формате int")
        if stud_id < 1:
            raise ValueError("Студент обязан иметь номер больше нуля")
        self.stud_id = stud_id

        if not isinstance(group, int):
            raise TypeError("Номер группы может быть только в формате int")
        if group < 1:
            raise ValueError("Группа обязана иметь номер больше нуля")
        self.group = group

        self.description = description

    def change_name_info(self, new_full_name: [str, str, str]) -> None:
        """
        Функция для изменения информаци об ФИО студента
        :param new_full_name: Измененное ФИО студента

        Примеры:
        >>> student = Student(full_name=['Иванова','Анна','Ивановна'],stud_id=1, group=10, sports=["Футбол","Баскетбол"], favorite_subject="history")
        >>> student.change_name_info(new_full_name=['Петрова', '', ''])
        """
        if not isinstance(new_full_name, list):
            raise TypeError("ФИО студента должно быть в формате [str,str,str]")
        if len(new_full_name) < 3:
            raise ValueError(
                "ФИО должно иметь 3 атрибута, даже если нет отчества в full_name должна передаваться пустая "
                "строка")
        if not all(isinstance(name, str) for name in new_full_name):
            raise TypeError("Фамилия, Имя и Отчество должны быть записаны в формате str")
        self.full_name = new_full_name

    def print_student_description(self) -> None:
        """
        Функция для вывода описания студента в удобном формате
        Пример:
        >>> student = Student(full_name=['Иванова','Анна','Ивановна'],stud_id=1, group=10, sports=["Футбол","Баскетбол"], favorite_subject="history")
        >>> student.print_student_description()
        sports: ['Футбол', 'Баскетбол']
        favorite_subject: history
        """
        for item, description in self.description.items():
            print(f"{item}: {description}")

    def move_to_another_group(self, new_group: int) -> None:
        """
        :param new_group: номер новой группы
        Пример:
        >>> student = Student(full_name=['Иванова','Анна','Ивановна'],stud_id=1, group=10, sports=["Футбол","Баскетбол"], favorite_subject="history")
        >>> student.move_to_another_group(100)
        """
        if not isinstance(new_group, int):
            raise TypeError("Номер группы может быть только в формате int")
        if new_group < 1:
            raise ValueError("Группа обязана иметь номер больше нуля")
        self.group = new_group


class Subject:
    def __init__(self, subj_name: str, subj_literature: str, who_study_it: list):
        """
        :param subj_name: Наименование предмета
        :param subj_literature: список литературы, изучаемой в этом курсе
        :param who_study_it: список групп, изучающих этот предмет
        Примеры:
        >>> physics = Subject(subj_name='Physics', subj_literature='Irodov-Posobie' , who_study_it=[1, 2, 3])
        """
        if not isinstance(subj_name, str):
            raise TypeError("Название предмета может быть только str")
        self.subj_name = subj_name

        if not isinstance(subj_literature, str):
            raise TypeError("Код предмета может быть только int")
        self.subj_literature = subj_literature

        if not isinstance(who_study_it, list):
            raise TypeError("Список групп изучающих предмет должен быть в формате list")
        self.who_study_it = who_study_it

    def add_new_group_to_subject(self, group_id: int) -> None:
        """

        :param group_id: номер группы которую хотим добавить
        Примеры:
        >>> physics = Subject(subj_name='Physics', subj_literature='Irodov-Posobie' , who_study_it=[1, 2, 3])
        >>> physics.add_new_group_to_subject(group_id=20)
        """
        if not isinstance(group_id, int):
            raise TypeError("Id группы может быть только в формате int")
        if group_id < 1:
            raise ValueError("id группы должно быть > 0")
        self.who_study_it.append(group_id)

    def delete_group(self, group_id_to_delete: int) -> None:
        """
         :param group_id_to_delete: номер группы которую хотим добавить
         Примеры:
         >>> physics = Subject(subj_name='Physics', subj_literature='Irodov-Posobie' , who_study_it=[1, 2, 3])
         >>> physics.delete_group(group_id_to_delete=1)
         """
        if not isinstance(group_id_to_delete, int):
            raise TypeError("Id группы может быть только в формате int")
        if group_id_to_delete < 1:
            raise ValueError("id группы должно быть > 0")
        self.who_study_it.pop(group_id_to_delete)
        ...

    def delete_literature(self, book: str):
        """
        :param book: имя книги которую хотим удалить из списка.
        >>> physics = Subject(subj_name='Physics', subj_literature='Irodov-Posobie' , who_study_it=[1, 2, 3])
        >>> physics.delete_literature('Irodov-Posobie')
        """
        if not isinstance(book, str):
            raise TypeError("Название книги только в формате str")

if __name__ == "__main__":
    doctest.testmod()