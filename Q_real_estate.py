class House:
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completion_year = completion_year

  def show_detail(self):
    print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("Shinjuku", "wood", "rent", "100,000yen", 2013)
house2 = House("Shibuya", "concret", "rent", "150,000yen", 2016)
house3 = House("Shinagawa", "wood", "buy", "3,000,000yen", 2020)

houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"There are {len(houses)} houses")
for house in houses:
  house.show_detail()