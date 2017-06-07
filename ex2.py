number = int(input("Give me a number... "))
check = int(input("And another... "))

if number % check == 0:
    print("%d evenly divides %d." % (check, number))
else:
    print("%d does not evenly divide %d." % (check, number))


# if int(number) % 4 == 0:
#     print("MULTIPLE OF 4!")
# elif int(number) % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
