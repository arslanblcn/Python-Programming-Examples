number = int(input("Please enter a number:"))
#check the number is bigger than 1 or not
if number > 1:
#try to find out the others values which can divisor to our number
    for i in range(2,number):
        if (number % i) == 0:
            print(number,"is not a prime")
            print(i,"times",number//i,"is",number)
            break
    else:
        print(number, "is a prime number...")
else:
    print("Please enter a number which is bigger than 1")
