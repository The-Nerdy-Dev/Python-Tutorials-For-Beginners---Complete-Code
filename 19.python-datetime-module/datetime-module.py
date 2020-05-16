
from datetime import datetime
import time

current_date = datetime.now()
print("Current Date:",current_date)


date_object = datetime(2020, 4, 4)
print(date_object)

date_time_object = datetime.strptime('2018/01/01',"%Y/%m/%d")

print(date_time_object)

print(date_time_object.year)
print(date_time_object.month)
print(date_time_object.strftime('%Y/%m'))

date_time_string = datetime.fromtimestamp(time.time())
print(date_time_string)
