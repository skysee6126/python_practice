# slice practice
inden = "990120-2324343"
print("sex :" + inden[7])
print("year :" + inden[0:2])
print("month :" + inden[2:4])
print("day :" + inden[4:6])
print("birthday :" +inden[:6])
print("personal num :" +inden[7:])
print("personal num :" +inden[-7:]) #from backside


#String related method
python = "Python is amazing"
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

#print(python.index("Java"))
print(python.find("Java"))

print(python.count("n"))



#String format
print("I'm a %d years old" %20)
print("I love %s" %"Python")
print("Apple is starting from %c" %"A")
print("I would like to take a %s and %s" %("coffee", "donuts"))

print("I'm a {}years old".format(20))
print("I would like to take a {} and {}".format("coffee", "donuts"))
print("I would like to take {1} and {0}".format("a coffee", "donuts"))

print("I'm a {age}years old and I love{fruit}".format(age =20, fruit="Apple"))

age = 20
fruit = "Apple"
print(f"I'm a {age}years old and I love{fruit}")


