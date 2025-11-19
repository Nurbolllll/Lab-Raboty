import json

class Student:
    def __init__(self, name, group, gpa):
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть от 0 до 4.")

    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}")


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        for s in self.students:
            if s.get_name() == name:
                self.students.remove(s)
                print(f"Студент '{name}' удалён.")
                return
        print(f"Студент '{name}' не найден.")

    def show_all(self):
        if not self.students:
            print("Группа пуста.")
        for s in self.students:
            s.display_info()

    def get_top_students(self, threshold):
        print(f"Студенты с GPA выше {threshold}:")
        for s in self.students:
            if s.get_gpa() > threshold:
                s.display_info()

    def save_to_file(self, filename):
        data = [
            {
                "name": s.get_name(),
                "group": s.get_group(),
                "gpa": s.get_gpa()
            }
            for s in self.students
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Файл {filename} сохранён.")


def menu():
    print("\n===== МЕНЮ =====")
    print("1 - Добавить студента")
    print("2 - Удалить студента")
    print("3 - Показать всех студентов")
    print("4 - Показать топ студентов (выше порога)")
    print("5 - Обновить GPA студента")
    print("6 - Сохранить в students.json")
    print("0 - Выход")
    return input("Выберите действие: ")


if __name__ == "__main__":
    group = Group()

    while True:
        choice = menu()

        if choice == "1":
            name = input("Введите имя студента: ")
            group_name = input("Введите группу: ")
            gpa = float(input("Введите GPA (0-4): "))
            student = Student(name, group_name, gpa)
            group.add_student(student)
            print("Студент добавлен.")

        elif choice == "2":
            name = input("Введите имя студента для удаления: ")
            group.remove_student(name)

        elif choice == "3":
            print("\nСписок студентов:")
            group.show_all()

        elif choice == "4":
            threshold = float(input("Введите порог GPA: "))
            group.get_top_students(threshold)

        elif choice == "5":
            name = input("Введите имя студента: ")
            for s in group.students:
                if s.get_name() == name:
                    new_gpa = float(input("Введите новый GPA: "))
                    s.update_gpa(new_gpa)
                    print("GPA обновлён.")
                    break
            else:
                print("Студент не найден.")

        elif choice == "6":
            group.save_to_file("students.json")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")