from datetime import datetime, timedelta
import time

dt_start = datetime(1998, 7, 1)
dt_now = datetime.now()
# dt = datetime.strptime("2022/01/01", "%y/%m/%d")
# dt = datetime.fromtimestamp(time.time())
duration = dt_now - dt_start

print(duration)
# print(f"{dt.year}/{dt.month}")
print("days", duration.days)
print("second", duration.seconds)
print("total second", duration.total_seconds())
