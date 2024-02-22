import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)
print(yesterday , today , tomorrow)