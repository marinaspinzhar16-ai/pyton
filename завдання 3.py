import re
def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до формату:
    +380XXXXXXXXX

    Видаляє всі символи, крім цифр та '+'.
    Якщо міжнародний код відсутній, додає '+38'.
    """

    # Видаляємо всі символи, крім цифр та '+'
    cleaned: str = re.sub(r"[^\d+]", "", phone_number.strip())

    # Якщо номер починається з '+'
    if cleaned.startswith("+"):
        digits: str = cleaned[1:]
    else:
        digits = cleaned

    # Якщо номер починається з 380 → додаємо тільки '+'
    if digits.startswith("380"):
        return f"+{digits}"

    # Якщо номер починається з 0 → додаємо '+38'
    if digits.startswith("0"):
        return f"+38{digits}"

    # Якщо номер без коду (наприклад 501234567) → додаємо '+38'
    return f"+38{digits}"
if __name__ == "__main__":
    examples = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    for number in examples:
        print(normalize_phone(number))
