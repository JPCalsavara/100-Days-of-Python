import random
import pandas as pd
import datetime as dt
import smtplib

my_email = "joaocalsavara456@gmail.com"
password = "mcxqyyhpclurmmej"

now = dt.datetime.today()
today = (now.month,now.day)

data = pd.read_csv("birthdays.csv")

birth_people ={(data_row.month,data_row.day):data_row  for (index, data_row) in data.iterrows()}

if today in birth_people:
    choose_letter = random.randint(1,3)
    # choose_letter = "of_love"
    birth_person = birth_people[today]
    with open(f"letter_templates/letter_{choose_letter}.txt") as letter:
        text = letter.read()
        text = text.replace("[NAME]",birth_person["name"])
        # print(name)
        # print(email)
        # print(text)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birth_person["email"],
            msg=f"Subject:Feliz Aniversario\n\n{text}")
            # msg=f"Subject:Te amo\n\n{text}")

