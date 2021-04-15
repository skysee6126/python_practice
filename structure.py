#String_list
subway = ["A","B","C"]
print(subway)

subway.append("D")
print(subway)

subway.insert(1, "F")
print(subway)

print(subway.pop())
print(subway)

subway.append("A")
print(subway.count("A"))


#Number_list
num_list = [3,4,5,2,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#num_list.clear()
#print(num_list)

#Mixed_list
num_list.extend(subway)
print(num_list)


#dictionary
cabinet = {3: "Apple", 2: "Orange"}
print(cabinet[3]) #error
print(cabinet.get(3)) #None
print(cabinet.get(5), "Empty") #default

print(3 in cabinet)
print(5 in cabinet)

cabinet[3] = "lemon"
cabinet[4] = "Strawberry"

print(cabinet)

del cabinet[4]
print(4)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)

#Tuple
menu = ("rice", "noodle")
print(menu[0])
print(menu[1])
#menu.add("bread") => cannot add new values

(name, age, hobby) = ("kim", 20, "soccer")
print (name, age, hobby)

#Set
#(not duplicate, no order)

my_set = {1,2,3,3,4,5}
print(my_set)

fruits = {"apple", "lemon", "tomato"}
veg = set(["tomato", "onion"])

#교집합
print(fruits & veg)
print(fruits.intersection(veg))

#합집합
print(fruits | veg)
print(fruits.union(veg))

#차집합
print(fruits - veg)
print(fruits.difference(veg))

veg.add("lemon")
print(veg)

veg.remove("lemon")
print(veg)


#change the structure
drink = {"coffe", "juice", "milk"}
print(drink, type(drink))

drink =list(drink)
print(drink, type(drink))

drink =tuple(drink)
print(drink, type(drink))
