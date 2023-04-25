import operator

arranged_books = dict(sorted(books.items(), key=operator.itemgetter(1)))
book_keys = list(arranged_books.keys())
# find the shortest book and print its title
# find the longest book and print its title
print(book_keys[0])
print(book_keys[-1])
