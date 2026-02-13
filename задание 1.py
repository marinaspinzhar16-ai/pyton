# https://github.com/marinaspinzhar16-ai/python
from datetime import datetime, date
datetime

def get_days_from_today(date_str: str) -> int:
    """
    Обчислює кількість днів між заданою датою та поточною датою.

    :param date_str: дата у форматі 'YYYY-MM-DD'
    :return: кількість днів (від'ємне число, якщо дата в майбутньому)
    """
    try:
        given_date: date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today: date = date.today()

        return (today - given_date).days

    except ValueError:
        raise ValueError("Невірний формат дати. Очікується 'YYYY-MM-DD'")



if __name__ == "__main__":
    example_date: str = "2021-10-09"
    result: int = get_days_from_today(example_date)

    print(f"Різниця в днях: {result}")
