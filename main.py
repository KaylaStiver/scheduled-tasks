##################### Extra Hard Starting Project ######################
import os
import datetime as dt
import random
import smtplib
import pandas

#Get current date and read birthdays in csv file.
today = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")

#Save all relevant columns to a list
birthdays_list = birthdays[["name", "email", "month", "day"]].values.tolist()

#Compare each birthdate month and day to today's month and day.
for birthday in birthdays_list:
    if today.month == birthday[2] and today.day == birthday[3]:
        #Choose a random letter and replace placeholder with name of birthday person.
        letter_num = random.randint(1,3)
        with open(f"./letter_templates/letter_{letter_num}.txt", mode="r") as file:
            letter_contents = file.read()
            letter_with_name = letter_contents.replace("[NAME]", birthday[0])

        email = os.environ.get("email")
        password = os.environ.get("password")

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=f"{birthday[1]}",
                                msg=f"Subject:Happy Birthday!!\n\n{letter_with_name}")
