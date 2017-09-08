number = input("please enter number: ")
number = int(number)
if number % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")

# for loop with else statement
for i in range(2, number // 2):
    if number % i == 0:
        break
else:
    print("your number is prime")
