a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Number please... "))
a_new = [x for x in a if x < number]
print("Numbers in my list less than %d \n" % number)
print(a_new)
