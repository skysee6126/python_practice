class ThailandPackage:
  def detail(self):
    print("Thailand tour, bangkok, 4days, 50,000yen")

if __name__ == "__main__":
  print("start Module directly")
  trip_to = ThailandPackage()
  trip_to.detail()
else:
  print("start Module from outside")