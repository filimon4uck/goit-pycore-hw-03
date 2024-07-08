from datetime import datetime, timedelta


def parse_from_string_to_datetime(string_date):
    return datetime.strptime(
        string_date, "%Y.%m.%d").date()


def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()
    week_later = today + timedelta(days=7)
    for user in users:
        original_birthday = parse_from_string_to_datetime(
            user["birthday"])
        birthday_this_year = datetime(
            today.year, original_birthday.month, original_birthday.day).date()
        if birthday_this_year < today:
            birthday_this_year = datetime(
                datetime.today().year + 1, original_birthday.month, original_birthday.day).date()

        if birthday_this_year >= today and birthday_this_year <= week_later:

            if birthday_this_year.weekday() >= 5:
                birthday_this_year = birthday_this_year + \
                    timedelta(days=(7 - birthday_this_year.weekday()))
                upcoming_birthdays.append(
                    {"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
    return upcoming_birthdays
