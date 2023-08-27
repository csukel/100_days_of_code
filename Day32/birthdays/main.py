##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
import pandas
from datetime import datetime
import random

data = pandas.read_csv("Day32/birthdays/birthdays.csv")
today = datetime.now()

df_birthdays = data[(data.month == today.month) & (data.day == today.day)]

for index, row in df_birthdays.iterrows():
    with open(
        f"Day32/birthdays/letter_templates/letter_{random.randint(1,3)}.txt"
    ) as file:
        content = file.read()
        content = content.replace("[NAME]", row["name"])
        print(content)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
