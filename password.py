#Making password program from URL
"""
rule
1) except "http://" part
2) except the part from the frist dot(.)
3) PW construction: frist 3 charter + the number of whole word + the number of 'e' in the word + "!"

"""

url = input()

index = url.index(".")
word = url[7:index]
#(or word = url.replace("http://", ""))
a = word[0:3]
b = len(word)
c = word.count("e")
d = "!"

pw = a + str(b) + str(c) + d
print(pw)