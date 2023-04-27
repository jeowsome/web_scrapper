word = input()
key = sum(int(input()).to_bytes(2, 'little'))

print(*[chr(ord(i) + key) for i in word], sep='')

