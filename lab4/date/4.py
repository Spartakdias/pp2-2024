import datetime

date1 = datetime.datetime.now()
date2 = date1 + datetime.timedelta(days = 1)
diff = date2 - date1
print(diff.total_seconds())