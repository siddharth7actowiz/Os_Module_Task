
import os

from datetime import datetime, timedelta

from calendar import *


#Taking User Input
current_date=input("Enter date to create folders of remaining days in year in YYYY-MM-DD:")
#to create files extensions
extensions=[".txt",".html",".py",".js"]

def create_files_inside_folders_date_name(current_date):
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
         os.makedirs(f"D:/Siddharth/files _with_dt_name_in_dt_folder/{folder_name}",exist_ok=True)

        #monthrange functon to find total days in a moth
        last_day_month=monthrange(folder_date.year,folder_date.month)[1]

        #current day for file
        day_in_file=(last_day_month-folder_date.day)+1

        #creates datetime object that will be rev for users current date
        rev_date=datetime(folder_date.year,folder_date.month,day_in_file)

        #formatting datetime object
        file_name=rev_date.strftime("%Y-%m-%d")

        for ext in extensions:
            file_path = f"D:/Siddharth/files _with_dt_name_in_dt_folder/{folder_name}/{file_name}{ext}"
            with open(file_path, "w") as f:
                f.write(f"{ext}")


#function call
create_files_inside_folders_date_name(current_date)
