def my_function():
    print("Hello from a function")
    i = 0
    while i < 100:
        i += 1
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
my_function()

# function with arguments
def arguments_functions(a, b, c):
    print(a)
    print(b)
    print(c)
arguments_functions("Muhammad", "Abyan", "Kamal")

# named parameters
def show_name(firstname,lastname, middlename):
    print(f"{firstname} {middlename} {lastname}")

show_name(lastname="Kamal", firstname="Muhammad", middlename="Abyan")

