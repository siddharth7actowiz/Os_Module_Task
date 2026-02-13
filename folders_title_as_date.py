import os
from datetime import datetime, timedelta,date

from calendar import *
#Taking User Input
current_date=input("Enter date to create folders of remaining days in year in YYYY-MM-DD:")

def create_folders_date_name(current_date):
    # getting todays_date from input
    todays_date=datetime.strptime(current_date,"%Y-%m-%d")

    #for current day nuber of year
    today_timetuple=todays_date.timetuple()
    curr_day_num=today_timetuple.tm_yday
    rem_days=365-curr_day_num

    #checking leap yaer
    if isleap(today_timetuple.tm_year):
        rem_days+=1

    for i in range(1,rem_days+1):
        folder_date=todays_date + timedelta(days= i)
        # converts datetime objet to string
        folder_name=datetime.strftime(folder_date,"%Y-%m-%d")
        # creating repositories
        print(folder_name)
        os.mkdir(f"D:/Siddharth/date_name_folder/date_folders/{folder_name}")

#function call
create_folders_date_name(current_date)
