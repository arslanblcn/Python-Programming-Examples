def square(squareCorner):
    print("Square's area is :",squareCorner**2)
    print("Square's perimeter is:",squareCorner*4)

def rectangle(shortCorner,longCorner):
    print("Rectangle's area is: ",shortCorner*longCorner)
    print("Rectangle's perimeter is:",(shortCorner*2)+(longCorner*2))

def circle(radius):
    pi = 3.14
    print("Circle's area is:",pi*(radius**2))
    print("Circle's perimeter is:",2*pi*radius)

print("[1] Square \n"
      "[2] Rectangle\n"
      "[3] Circle\n")
while True:
    print("\nEnter 0 for stop the program...")
    answer = int(input("\nSelect the figure: "))
    if answer == 1:
        squareCorner = int(input("Enter the square corner:"))
        square(squareCorner)
    elif answer == 2:
        shortCorner = int(input("Enter the short corner of rectangle: "))
        longCorner = int(input("Enter the long corner of rectangle: "))
        rectangle(shortCorner,longCorner)
    elif answer == 3:
        radius = int(input("Enter the radius:"))
        circle(radius)
    elif answer == 0:
        break
    else:
        print("Choose a number between 1-3")