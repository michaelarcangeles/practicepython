number = int(input("Number please... "))
nums = range(1, number)
divisors = [x for x in nums if number % x == 0]
print(divisors)
