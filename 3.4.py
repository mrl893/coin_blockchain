print("welcome to Py Pizza Deliveries! ")
size = input("What size pizza do you want? s, m, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? y or N ")



bill = 0

if  size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")
