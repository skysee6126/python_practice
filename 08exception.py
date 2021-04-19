try:
  print ("This is a calculator for divition")
  num1 = int(input("please fill in the number :"))
  num2 = int(input("please fill in the number :"))
  print (num1/num2)
except ValueError:
  print("Please check your input text")
except ZeroDivisionError as err:
  print(err)


#list err
try:
  print ("This is a calculator for multiplication")
  nums = []
  nums.append(int(input("please fill in the number :")))
  nums.append(int(input("please fill in the number :")))
  nums.append(int(nums[0]/nums[1]))
  print (f"{nums[0]}/{nums[1]} = {nums[2]}")
except Exception as err:
  print("Unknown Error")
  print(err)

# Raising err
try:
  print ("This is a calculator for single-digit divition")
  num1 = int(input("please fill in the number :"))
  num2 = int(input("please fill in the number :"))
  if num1 >= 10 or num2 >= 10:
    raise ValueError
  print (num1/num2)
except ValueError:
  print("Only single-digit is allowed")

#User 
class BigNumberError(Exception):
  def __init__(self, msg):
    self.msg = msg
  def __str__(self):
    return self.msg

try:
  print ("This is a calculator for single-digit divition")
  num1 = int(input("please fill in the number :"))
  num2 = int(input("please fill in the number :"))
  if num1 >= 10 or num2 >= 10:
    raise BigNumberError(f"Input value is {num1}, {num2}")
  print (num1/num2)
except ValueError:
  print("Only single-digit is allowed")
except BigNumberError as err:
  print("Please check the number, it allows only single-digit")
  print(err)
finally:
  print("Thanks")
