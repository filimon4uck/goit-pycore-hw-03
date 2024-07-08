from datetime import datetime


def get_days_from_today(date):
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        return (current_date - converted_date).days

    except ValueError:
        print("Date is not correct")
