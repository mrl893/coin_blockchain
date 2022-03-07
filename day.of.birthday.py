import datetime
import time
print("**************************************************************")
print("Input 1 if you want to know how many days in your birth year.")
print("**************************************************************")
birth_day =int(input("Input day of your Birthday"))
day=int(datetime.date.today().day)
month=int(datetime.date.today().month)
year=int(datetime.date.today().year)
nomber=int(input("Input what do you want to know"))

if month > birth_month:
    age=year - birth_year
else:
    age=(year - birth_year) - 1
if (nomber > 0) and (nomber < 3) and (age > 0) and (age < 130):
    if number == 1:
        if birth_year % 4 != 0:
            print("It is leap year")
        else:
            print("it is not leap year")
    if number == 2:
        print("You are grupe:", end="")
        if age < 1:
            print("You are baby")
        elif (age >= 1) and (age < 3):
            print("You are older than baby")
        elif  (age >= 3) and (age < 5):
            print("You are Kindergarteners")
        elif (age >= 5) and (age < 12):
            print("You are schoolchild")
        elif (age >= 12) and (age < 19):
            print("You are teenager")
        elif (age > 19):
            print("You are adult")
