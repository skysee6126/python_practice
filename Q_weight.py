def std_weight(height, gender):
  if gender == "male":
    return height*height*22
  else:
    return height*height*21


height = 175
gender = "male"
weight = round(std_weight(height/100, gender), 2)

print (f"The standard height for height {height}cm is {weight}kg")

