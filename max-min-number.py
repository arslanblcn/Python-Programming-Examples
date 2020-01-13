number = int(input("Please enter a number :"))
maxNumber = number
minNumber = number

while (number > 0):
    if(number > maxNumber):
        maxNumber = number
    if(number < minNumber):
        minNumber = number
    number = int(input("Please enter a number :"))

print("Max number is : {}".format(maxNumber))
print("Min number is : {}".format(minNumber))

