
import os
from datetime import datetime, timedelta,date
todays_date=date(2026,2,13)
today=datetime.now().timetuple()
print()

for i in range(today.tm_yday,365+1):
    folder_date=todays_date + timedelta(days= i- 1)

    folder_name=datetime.strftime(folder_date,"%Y %m %d")
    os.mkdir(f"D:/Siddharth/os_module_task/{folder_name}")


