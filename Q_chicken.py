class SoldOutError(Exception):
  pass


chicken = 10
waiting = 1
while (True):
  try:
    print(f"last chicken: {chicken}")
    order = int(input("How many karaage do you want?"))
    if order > chicken:
      print("ran out of ingredients") 

    elif order <= 0:
      raise ValueError

    else:
      print(f"the order {order} is accepted for waiting number {waiting}")
      waiting += 1
      chicken -= order
    if chicken == 0:
      raise SoldOutError()

  except ValueError:
    print("You put the wrong number")
  except SoldOutError:
    print("ran out of ingredients so that you cannot order today anymore")
    break
