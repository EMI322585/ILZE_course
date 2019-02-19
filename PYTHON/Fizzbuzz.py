print("This iz FizzBuzz game:")
x = input("Please enter a number between 1 and 100:")
x = int(x)
for x in range(1,x+1):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)