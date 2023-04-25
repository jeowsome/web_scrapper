# put your python code here
words = input().lower().split(" ")
parsed_words = {word: words.count(word) for word in words}

for word, count in parsed_words.items():
    print(word, count)