class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Person):
    def __init__(self, name, age, group, gpa):
        super().__init__(name, age)
        self.group = group
        self.gpa = gpa

    def display_info(self):
        return (f"Студент: {self.name}, Возраст: {self.age}, "
                f"Группа: {self.group}, Средний балл: {self.gpa}")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        return (f"Преподаватель: {self.name}, Возраст: {self.age}, "
                f"Предмет: {self.subject}, Стаж: {self.experience} лет")


class AdminStaff(Person):
    def __init__(self, name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def display_info(self):
        return (f"Админ. сотрудник: {self.name}, Возраст: {self.age}, "
                f"Должность: {self.position}, Отдел: {self.department}")


# -------------------------- СПИСОК ЛЮДЕЙ --------------------------

people = []


# -------------------------- ФУНКЦИИ МЕНЮ --------------------------

def add_person():
    print("\nКого добавить?")
    print("1 — Студент")
    print("2 — Преподаватель")
    print("3 — Администратор")

    choice = input("Выбор: ").strip()

    name = input("Имя: ")
    age = input("Возраст: ")

    if choice == "1":
        group = input("Группа: ")
        gpa = float(input("Средний балл: "))
        obj = Student(name, age, group, gpa)

    elif choice == "2":
        subject = input("Предмет: ")
        experience = int(input("Стаж: "))
        obj = Teacher(name, age, subject, experience)

    elif choice == "3":
        position = input("Должность: ")
        department = input("Отдел: ")
        obj = AdminStaff(name, age, position, department)

    else:
        print("Неверный выбор!")
        return

    people.append(obj)
    print("Добавлено!")


def show_people():
    if not people:
        print("\nСписок пуст.")
        return

    print("\n===== СПИСОК ЛЮДЕЙ =====")
    for i, p in enumerate(people, 1):
        print(f"{i}. {p.display_info()}")


def delete_person():
    show_people()
    if not people:
        return

    num = int(input("\nНомер для удаления: ")) - 1

    if 0 <= num < len(people):
        people.pop(num)
        print("Удалено!")
    else:
        print("Неверный номер.")


def edit_person():
    show_people()
    if not people:
        return

    num = int(input("\nНомер для изменения: ")) - 1

    if not (0 <= num < len(people)):
        print("Неверный номер.")
        return

    person = people[num]

    print("\nВведите новые данные:")
    person.name = input("Имя: ")
    person.age = input("Возраст: ")

    if isinstance(person, Student):
        person.group = input("Группа: ")
        person.gpa = float(input("Средний балл: "))

    elif isinstance(person, Teacher):
        person.subject = input("Предмет: ")
        person.experience = int(input("Стаж: "))

    elif isinstance(person, AdminStaff):
        person.position = input("Должность: ")
        person.department = input("Отдел: ")

    print("Изменено!")


# -------------------------- МЕНЮ --------------------------

def main():
    while True:
        print("\n===== УЧЕБНОЕ ЗАВЕДЕНИЕ =====")
        print("1 — Добавить человека")
        print("2 — Удалить человека")
        print("3 — Изменить человека")
        print("4 — Показать всех")
        print("0 — Выход")

        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            add_person()
        elif choice == "2":
            delete_person()
        elif choice == "3":
            edit_person()
        elif choice == "4":
            show_people()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()