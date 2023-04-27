import string

# put your code here
print(*[input().capitalize() if not i else string.capwords(input()) for i in range(2)], sep="\n")
