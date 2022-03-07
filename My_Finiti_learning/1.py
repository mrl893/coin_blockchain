2+2
input("Enter your name: ")
my_name = input("Enter your name: ")

file = open("name.txt", mode="w")
file.write(my_name)

file.close()
file = open("name.txt", mode="r")
print(file.read())



