
name = input("Please enter your name: ")
print("Hello %s" % name)

number = input("Please enter number: ")
try:
    number = int(number)
except ValueError:
    print("%s is not number" % number)
else:
    print("Your number is %d" % number)
