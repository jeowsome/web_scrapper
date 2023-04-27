import string

template = string.Template("Hi, $name! You look $adjective today! You're doing great!")
compliment = template.substitute(name=input(), adjective=input())
print(compliment)
