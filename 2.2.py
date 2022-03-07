height =  input("Enter Your height in M: ")
weight = input("Enter Your weight in KG:  ")

weights =  int(weight)
heights = float(height)

ibm = weights / heights ** 2
ibm = weights / (heights * heights)
ibms = int(ibm)
print(ibms)

