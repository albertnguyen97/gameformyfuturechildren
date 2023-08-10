import random
import smtplib
import pandas
from datetime import datetime
today = (datetime.now())
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

my_email = "chaunm.hmc@gmail.com"
password = "fakepassword" # in app passwords

new_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}

if today_tuple in new_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = new_dict[today_tuple]
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday! \n\n {contents}")
        connection.close()