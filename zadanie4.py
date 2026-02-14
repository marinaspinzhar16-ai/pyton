from datetime import datetime, date, timedelta
from typing import List, Dict
def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Повертає список користувачів, яких потрібно привітати
    протягом наступних 7 днів (включаючи сьогодні).

    Якщо день народження припадає на вихідний,
    дата привітання переноситься на понеділок.
    """

    today: date = datetime.today().date()
    upcoming_birthdays: List[Dict[str, str]] = []

    for user in users:
        birthday: date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження у поточному році
        birthday_this_year: date = birthday.replace(year=today.year)

        # Якщо вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days: int = (birthday_this_year - today).days

        # Перевірка чи входить у 7 днів (включаючи сьогодні)
        if 0 <= delta_days <= 7:

            congratulation_date: date = birthday_this_year

            # Якщо субота (5) → +2 дні
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            # Якщо неділя (6) → +1 день
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

if __name__ == "__main__":
    users_data = [
        {"name": "Anna", "birthday": "1990.03.12"},
        {"name": "John", "birthday": "1985.03.15"},
        {"name": "Maria", "birthday": "1992.03.16"},
    ]

    result = get_upcoming_birthdays(users_data)

    for item in result:
        print(item)
