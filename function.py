def function():
    print("Hello")

function()

choice = int(input("Enter the Choice : "))
def function(choice):
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("fizbuzz")
        elif num % 5 == 0:
            print("buzz")
        elif num % 3 == 0:
            print("fizz")
        else:
            print(num)

function(choice)