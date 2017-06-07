
def get_divisors(num):
    nums = range(1, num + 1)
    divisors = [x for x in nums if num % x == 0]
    return divisors

num = int(input("Number please... "))
divisors = get_divisors(num)
print(divisors)
if len(divisors) == 2 and num in divisors and 1 in divisors:
    print("PRIME")
else:
    print("NOT PRIME")
