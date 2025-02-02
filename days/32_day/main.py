import random
import smtplib
#smtplib create a route to unite e-mail
import datetime as dt

my_email = "joaocalsavara456@gmail.com"
password = "mcxqyyhpclurmmej"
#
# #connection = smtplib.SMTP("smtp.gmail.com", port=587)
# #connection.close()
# #it can use the same method likes a file
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
# #Encripted for protection tls
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="joaocalsavara456@yahoo.com",
#         msg="Hello")

# now = dt.datetime.now()
# year = now.year
# print(year)
#datetime is the main class
#.now() - all information 2025-02-02 13:10:32.264967
#.year .day .month for specific data as an attribute

#Create an object with parameters
# date_of_birth = dt.datetime(year=2006,month=5,day=4,hour=6)
# print(date_of_birth)

now = dt.datetime(year=2025,month=2,day=4)
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 1:
    with open("quotes.txt") as file:
        frases = file.readlines()
        choose_frase = random.choice(frases)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="joaocalsavara456@yahoo.com",
                msg=f"Subject:Monday Motivation\n\n{choose_frase}")