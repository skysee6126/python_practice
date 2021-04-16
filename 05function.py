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

def profile(name, age, lang):
  print(f"name: {name} \t age: {age} \t language: {lang}")

profile("A", 20, "KR")
profile("B", 25, "JP")