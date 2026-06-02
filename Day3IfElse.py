#simple python learning example 
def greet(name):
    print(f"Hello,{name}! WELCOME TO PYTHON PROGRAM")
    name = input("Enter your name.......!")
    greet (name)
    Age = int(input("Enter your Age:..........."))
    if Age>=18:
        print("you are an adult.")
    else:
        print( "you are a minor")
        print("\nCounting  of number from 1 to5:")
        for i in range(1,6):
         print(i)
        print("\nSquares of number from 1 to5:")
for  i in range(1,6):
    print(f"{i}² = {i**2}")        