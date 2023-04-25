import operator

# write your code here
sorted_students = dict(sorted(student_list.items(), key=operator.itemgetter(1)))
print(list(sorted_students.keys())[0])