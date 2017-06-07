
name = input("What is your name? ")
age = input("Hi %s! How old are you? " % name)
year = (100 + (2017 - int(age)))
message = "%s, you will be 100 years old in the year %d!" % (name, year)
print(message)

number = input("Give me a number... ")
print(int(number) * (message + '\n'))
