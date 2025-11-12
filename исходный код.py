import logging

# Настройка логирования (создаёт файл errors.log)
logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - ERROR - %(message)s"
)

def main():
    try:
        # Ввод данных от пользователя
        P = float(input("Введите сумму вклада: "))
        r = float(input("Введите годовую процентную ставку (%): "))
        t = float(input("Введите срок вклада (в годах): "))

        # Проверка на отрицательные значения
        if P <= 0 or r <= 0 or t <= 0:
            raise ValueError("Все значения должны быть положительными.")

        n = 12  # количество начислений в год
        r = r / 100  # перевод процентов в доли

        # Формула сложных процентов
        S = P * (1 + r / n) ** (n * t)
        S = round(S, 2)

        print(f"\nИтоговая сумма через {t} лет: {S} тг")

        # Запись результата в файл result.txt
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(f"Вклад: {P} тг\n")
            file.write(f"Ставка: {r * 100}%\n")
            file.write(f"Срок: {t} лет\n")
            file.write(f"Итоговая сумма: {S} тг\n")

        print("Результаты сохранены в файл result.txt")

    except ValueError:
        print("Ошибка: введите числовые значения больше нуля.")
        logging.error("Некорректный ввод данных (буквы или отрицательные значения).")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
        logging.error("Ошибка деления на ноль при вычислениях.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        logging.error(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()