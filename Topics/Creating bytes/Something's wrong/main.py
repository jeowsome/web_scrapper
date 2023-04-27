number = int(input())
bytes_number = number.to_bytes(5, 'big')
number_from_bytes = int.from_bytes(bytes_number, 'big')
print(number == number_from_bytes)  # <-- expected to be True!