import smtplib
import datetime as dt
import random

# ------------------------Constants---------------------------------------------------#

MY_EMAIL = "" #  Your Email
PASSWORD = "" #  Your Password
DATE = dt.datetime.now()
DAY = DATE.day
RANDOM_NUM = random.randint(1, 102)

if DAY == 2:
    with open("quotes.txt") as quotes:
        quote_list_rough = list(quotes.readlines())
        quote_list = []
        for quote in quote_list_rough:
            quote_list.append(quote.replace("\n", ""))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="sidestewbrew@yahoo.com",
                            msg=f"Subject:Motivational Monday\n\n{quote_list[RANDOM_NUM]}")
