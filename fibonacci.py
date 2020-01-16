def fibonacci(n):
    total = 0
    firstNum = 1
    secondNum = 0
    for i in range(n):
        print(total)
        total = firstNum + secondNum
        firstNum = secondNum
        secondNum = total
    #We calculated fibonacci series by for loop
serieNum = int(input("How long do you want fibonacci series:"))
fibonacci(serieNum)
#We sent the value of user to the function