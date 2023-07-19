# Seth Jacobs Fizz (divisiable by 3) Buzz (divisable by 5) challenge
for i in range(1,100,1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



