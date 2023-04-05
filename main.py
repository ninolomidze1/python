# 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


number = 5
print("is number == 5 ? I predict yes")
print(number == 5)
print("is number == 6 ? i predict False")
print(number == 6 )

print(10 > 5)
print('Odd' == 'Odd')
print(["Tom","Nick", "Jane"] == ["Tom","Nick", "Jane"])
print(True or False)
print(2 + 2 == 5)
print(20 < 5)
print('hello' == 'bye')
print({'a': 1} == {'a': 2})

# 2

print('Blue' == 'Blue')  # True
print('Blue' != 'Red')  # True
print('blue' == 'Blue')  # False
print('Blue' != 'Blue')  # False

print('BLUE'.lower() == 'red')  # True
print('blue'.lower() == 'red')  # False

print(5 == 5)  # True
print(5 != 5)  # False
print(5 > 3)  # True
print(5 < 3)  # False
print(5 >= 5)  # True
print(5 <= 3)  # False

print(5 > 3 and 2 < 4)  # True
print(5 > 3 and 2 > 4)  # False
print(5 > 3 or 2 > 4)  # True
print(5 < 3 or 2 > 4)  # False

fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)  # True
print('grape' in fruits)  # False

languages = ['Spanish', 'English', 'Georgian']
print('Russian' not in languages)  # True
print('Georgian' not in languages)  # False

# 5.3.4

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color != "green":
    print("Congratulations! You just earned 10 points.")
else:
    print(" ")

# 5.5

alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == "yellow":
    print("Congratulations! You just earned 10 points.")
elif alien_color == "red":
    print("Congratulations! You just earned 15 points.")
else:
    print(" ")

# 5.6
age = 70

if age < 2:
    print("the person is a baby.")
elif 2 <= age < 4:
    print("the person is a toddler.")
elif 4 <= age < 13:
    print("the person is a kid.")
elif 13 <= age < 20:
    print("the person is a teenager.")
elif 20 <= age < 65:
    print("the person is an adult.")
else:
    print("that the person is an elder.")

# 5.7
fruits = ['apple', 'banana', 'grape']

if 'apple' in fruits:
    print("I like apples!")
    
if 'orange' in fruits:
    print("I like oranges!")
    
if 'banana' in fruits:
    print("I like bananas!")
    
if 'mango' in fruits:
    print("I like mangos!")


# 5.8

usernames = ['Nino', 'Anna', 'Nick', 'Admin', 'Lily']

for username in usernames:
    if username == 'Admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again.")

# 5.9

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")


# 5.10
current_users = ["Lika", "Luka", "Sandro", "Mari", "Sally"]
new_users = ["Jon", "Luka", "Nick", "Mary", "Ani"]
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, username '{user}' is already taken. Please choose a new username.")
    else:
        print(f"Username '{user}' is available.")

# 5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")


# 4

fruits = [
   ["Apple -", 3.2],
   ["Grape -", 4.0],
   ["Banana -", 2.8],
   ["Pineapple -", 1.7],
   ["Kiwi -", 3.5]
]

for fruit in fruits:
    print(fruit[0], fruit[1])


name = ["apple", "grape", "banana", "pineapple", "kiwi"]
price = [3.2, 4.0, 2.8, 1.7, 3.5]

for i in range(len(name)):
    print(name[i] + " " + str(price[i]))
