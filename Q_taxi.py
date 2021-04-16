from random import *

result = 0

for i in range (1 ,11):
  duration = randint(5,50)
  if 5 <= duration <= 15:
    print (f"[O] {i} guest (duration: {duration})")
    result += 1
  else:
    print (f"[ ] {i} guest (duration: {duration})")

print(f"total number of guests:{result}")