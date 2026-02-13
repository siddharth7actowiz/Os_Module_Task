import os
from datetime import datetime, timedelta,date


def create_folders_date_name():
    # getting todays_date
    todays_date=date(2026,2,13)
    # for current day nuber of year
    today_timetuple=datetime.now().timetuple()


    for i in range(1,320):
        folder_date=todays_date + timedelta(days= i)
        # converts datetime objet to string
        folder_name=datetime.strftime(folder_date,"%Y %m %d")
        # creating repositories
        os.mkdir(f"D:/Siddharth/os_module_task/{folder_name}")

#function call
create_folders_date_name()