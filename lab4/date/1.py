import datetime

today = datetime.date.today()
five_days = datetime.timedelta(days = 5)
print(today - five_days)