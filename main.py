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
