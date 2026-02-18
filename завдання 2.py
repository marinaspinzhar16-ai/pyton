import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.

    Параметри:
    min (int): мінімальне можливе число (не менше 1)
    max (int): максимальне можливе число (не більше 1000)
    quantity (int): кількість чисел для вибору

    Повертає:
    list: відсортований список унікальних випадкових чисел
          або порожній список, якщо параметри некоректні
    """

    # Перевірка валідності параметрів
    if (
        not isinstance(min, int) or
        not isinstance(max, int) or
        not isinstance(quantity, int) or
        min < 1 or
        max > 1000 or
        min > max or
        quantity < 1 or
        quantity > (max - min + 1)
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
