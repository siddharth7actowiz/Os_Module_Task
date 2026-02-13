import os
from datetime import datetime, timedelta,date
from os.path import exists

#Taking User Input
current_date=input("Enter date to create folders of remaining days in year in YYYY-M-D:")

def create_folders_date_name(current_date):
    # getting todays_date from input
    todays_date=datetime.strptime(current_date,"%Y %m %d")

    #for current day nuber of year
    today_timetuple=datetime.now().timetuple()
    curr_day_num=today_timetuple.tm_yday
    rem_days=365-curr_day_num

    for i in range(rem_days):
        folder_date=todays_date + timedelta(days= i)
        # converts datetime objet to string
        folder_name=datetime.strftime(folder_date,"%Y %m %d")
        # creating repositories
        os.makedirs(f"D:/Siddharth/os_module_task/{folder_name}",exist_ok=True)

#function call
create_folders_date_name(current_date)
