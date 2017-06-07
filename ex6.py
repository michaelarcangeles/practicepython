word = input("Word please... ")

a = list(word)
b = list(word)
b.reverse()

print(a)
print(b)

if a == b:
    print("%s is a PALINDROME!" % word)
else:
    print("%s is not a palindrome." % word)
