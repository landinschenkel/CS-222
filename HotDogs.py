#   Name: Landin Schenkel
#   Assignment: 2
#   Program Name: HotDogs
#   Date: 08/26/25

hotDogPack = 10
bunPack = 8
totalHotDogs = 0
leftOverHot = 0
leftOverBun = 0
requiredHot = 0
requiredBun = 0
people = 0
z = 0
e = 0


people = int(input("How many people will be at this party: "))
z = int(input("How many hot dogs will each person eat: "))

totalHotDogs = people * z

requiredHot = (totalHotDogs + hotDogPack - 1) // hotDogPack
requiredBun = (totalHotDogs + bunPack - 1) // bunPack

leftOverHot = requiredHot * hotDogPack - totalHotDogs
leftOverBun = requiredBun * bunPack - totalHotDogs

print("\nCookout Planning Summary: ")
print("Minimum number of hot dog packs needed needed: ", requiredHot)
print("Minimum number of hot dog bun packs needed: ", requiredBun)
print("Number of leftover hot dogs: ", leftOverHot)
print("Number of leftover hot dog buns: ", leftOverBun)