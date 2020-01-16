from random import randint
counter = 0
randValue = randint(1,50)
userValue = int(input("Guess the number :"))
#we have determined user's value and random value

while userValue != randValue:
    #Program will be working until userValue and randValue will be equal

    if userValue < randValue:
        userValue = int(input("You should enter a larger number than you did:"))
        counter += 1
    if userValue > randValue:
        userValue = int(input("You should enter a smaller number than you did:"))
        counter += 1
    #We check it out which one is large or small and our counter is increasing one by one

print("Congarts!! you found it",counter+1,"attempts")