# main.py

def calculate_average(grades: list) -> float:
    """Возвращает среднее значение списка оценок."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def determine_grade_letter(average: float) -> str:
    """Определяет буквенную оценку по среднему баллу."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def student_report(name: str, grades: list) -> str:
    """Формирует строку отчёта об успеваемости студента."""
    avg = calculate_average(grades)
    letter = determine_grade_letter(avg)

    return f"Student: {name}, Average: {avg:.2f}, Grade: {letter}"


if __name__ == "__main__":
    try:
        name = input("Введите имя студента: ")
        grades_input = input("Введите оценки через пробел: ")
        grades = list(map(int, grades_input.split()))

        print(student_report(name, grades))

    except Exception as e:
        print("Ошибка:", e)
