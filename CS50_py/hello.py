#Ask User for name
name = input("What's your name? ").strip().title()

#Split user's name into first and last name
first, last = name.split(" ")

#Say hello to user
print("hello", first, last)