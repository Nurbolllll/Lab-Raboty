def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)
num = 10
print(f"Сумма чисел от 1 до {num} равна {recursive_sum(num)}")	
