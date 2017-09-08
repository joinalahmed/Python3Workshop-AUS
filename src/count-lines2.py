filename = input("Please enter your filename: ")
fo = open(filename, "r")
counter = 0
while True:
    line = fo.readline()
    if not line:
        break
    counter += 1
    print(line)
print(counter)
