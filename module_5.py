#List
fruits = ["apple", "pear", "banana"]

for fruit in range(0, len(fruits)):
    print(fruits[fruit])

for fruit in fruits:
    print(fruit)
    
    
for char in "Hello Jordan":
    print(char)


for i in range(10):
    print((i+1)*(i+1))



print(fruits)

fruits.append("rasberry")

print(fruits)

fruits[1] = "orange"

print(fruits)
print(fruits[1])

if "strawberry" in fruits:
    print("This is in fruits")
    fruits.remove(fruits[2])
    
print(fruits)

#tuple
newFruits = ("guava", "mango", "pineapple")

#dictionary
worldFoods = {"italy":"pizza", "spain":"paella", "mexico":"tacos"}

print(worldFoods["spain"])

worldFoods["france"] = "croissants"
worldFoods.update({"japan":"ramen", "america":"hamburgers"})

print(worldFoods)

for key in worldFoods.keys():
    print(key, ":", worldFoods[key])
