class Bike(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    
class Bike_shop(object):
  def __init__(self, name, margin, initial_inventory):
    self.name = name
    self.margin = margin
    self.inventory = initial_inventory
    self.prices = {}
    for bikes in self.inventory:
      self.prices[bikes.model] = bikes.cost * (1+self.margin)
    self.profit = 0
    
  def add_stock(self, bikes):
    self.inventory.extend(bikes)
    for bikes in self.inventory:
      self.prices[bikes.model] = bikes.cost * (1+self.margin)
  
  def sell(self, bikes):
    if bikes
    for bikes in bikes:
      self.inventory.remove(bikes)
      self.profit += (bikes.cost * self.margin)
      print "We've sold a bike for $" + str(bikes.cost * self.margin)
    print "We've sold $" +str(self.profit)+ " total"
    
    
class Customer(object):
  def __init__(self, name, fund):
    self.name = name
    self.fund = fund
  
  def buy(self, bike, store):
    self.owned = bike
    self.fund -= store.prices[bike.model]
    print "I bought " + bike.model + " and I have $" + self.fund + " left in my fund!"

model1 = Bike("Model1", 30, 400)
model2 = Bike("Model2", 25, 500)
model3 = Bike("Model3", 20, 600)
model4 = Bike("Model4", 20, 750)
model5 = Bike("Model5", 18, 1000)
model6 = Bike("Model6", 16, 1500)
bike_list = [model1, model2, model3, model4, model5, model6]

jareds = Bike_shop("Jareds", .2, bike_list)

customerA = Customer("Aaron", 500)
customerB = Customer("Becky", 800)
customerC = Customer("Chris", 2000)
customer_list = [customerA, customerB, customerC]

def can_buy(customer, store): 
  affordable = []
  print customer.name + " has $" + str(customer.fund) + " and can buy the following from " + store.name + ":"
  for model, price in store.prices.iteritems():
    if customer.fund >= price:
      affordable.append(model)
      print model + " for $" + str(price)
      
def buy (customer, bike, store):
  store.sell(bike)
  customer.buy(bike, store)

if __name__ == "__main__":
  for customer in customer_list:
    can_buy(customer, jareds)
  
  print "Jared's currently has " + ", ".join([bike.model for bike in jareds.inventory]) + " in stock"
  
  jareds.sell([model1])
  #buy(customerA, model1, jareds)
  #buy(customerB, [model3], jareds)
  #buy(customerC, [model5], jareds)
