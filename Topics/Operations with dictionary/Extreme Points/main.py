from operator import itemgetter
# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'

# Option A
# sorted_dict = dict(sorted(test_dict.items(), key=itemgetter(1)))
# dict_keys = list(sorted_dict.keys())
# print("min:", dict_keys[0])
# print("max:", dict_keys[-1])

# Option B
print("min:", min(test_dict, key=test_dict.get))
print("max:", max(test_dict, key=test_dict.get))
