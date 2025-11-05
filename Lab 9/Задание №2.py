def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    max_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_rest else max_rest
numbers = [4, 15, 2, 9, 30, 7, 22]
print("Максимальное число в списке:", find_max(numbers)) 
