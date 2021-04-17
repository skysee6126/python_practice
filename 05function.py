def open_account():
  print ("created new account")

open_account()


def deposit(balance, money):
  print(f"total amount:{balance+money}")
  return balance + money

def withdraw(balance, money):
  if balance >= money:
    print(f"completed withdraw, total amount:{balance-money}")
    return balance - money
  else:
    print(f"Check the balance, total amount:{balance}")
    return balance

def withdraw_night(balance, money):
  commission = 100
  return commission, balance -money -commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 100)
commission, balance = withdraw_night(balance, 500)
print(f"commission: {commission}, total amount: {balance}")

def profile(name, age=17, lang="EN"):
  print(f"name: {name} \t age: {age} \t language: {lang}")

profile("A", 20, "KR")
profile("B", 25, "JP") 
profile("C") 
profile(age=23, name= "D") 

def spec(name, *lang):
  print("name:{0}\t".format(name), end="")
  for i in lang:
    print(i, end=" ")
  print()

spec("A", "EN", "KR", "JP", "DE")
spec("B", "EN", "EP", "JP")


#변수 앞에서 global을 붙이면 함수 내에서 지역변수로도 사용가능
#함수 내에서 변경된 값을 전역 변수에서도 반영하기 위해서는 return