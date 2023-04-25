# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
parsed_dict = {i.upper(): i.lower() for i in some_iterable}
print(parsed_dict)
