
def fib_nums(length):
    count = 0
    nums = [0, 1]
    while count < length - 1:
        next_sum = nums[count] + nums[len(nums) - 1]
        nums.append(next_sum)
        count += 1
    print(nums[1:])

length = int(input("Sequence length: "))
fib_nums(length)
