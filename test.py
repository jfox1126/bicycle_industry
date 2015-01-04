import random

#Bike class and 6 created 'Bike' objects
class Bike(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost

model1 = Bike("Model1", 30, 400)
model2 = Bike("Model2", 25, 500)
model3 = Bike("Model3", 20, 600)
model4 = Bike("Model4", 20, 750)
model5 = Bike("Model5", 18, 1000)
model6 = Bike("Model6", 16, 1500)
bike_list = [model1, model2, model3, model4, model5, model6]
    
#Bike Shop class and 1 created 'Bike Shop' Object
class Bike_shop(object):
  def __init__(self, name, margin, initial_inventory):
    self.name = name
    self.margin = margin
    self.inventory = {}
    for bike, stock in initial_inventory.iteritems():
      self.inventory[bike] = {
        "stock": stock,
        "price": bike.cost * (1+self.margin)
      }
    self.profit = 0
    
  def print_inventory(self):
    print self.name +" currently has the following in stock:"
    for bike in self.inventory:
      print bike.model + ": " + str(self.inventory[bike]["stock"])
    print ""
  
  def sell(self, bike):
    self.inventory[bike]["stock"] -= 1
    self.profit += (bike.cost * self.margin)
    print self.name + " sold a " + bike.model + " bike for $" + str(self.inventory[bike]["price"]) + "! That's a $" + str(bike.cost * self.margin) + " profit"
    print ""

  def print_profit(self):
    print self.name + " has made $" + str(self.profit) + " total"
    print ""
    
inventory2 = {
  model1: 1,
  model2: 1,
  model3: 1,
  model4: 1,
  model5: 1,
  model6: 1,
}

jareds = Bike_shop("Jared's", .2, inventory2)

#Customer class and 3 'Customer' Objects
class Customer(object):
  def __init__(self, name, fund):
    self.name = name
    self.fund = fund
    self.affordable = []
    self.owned = []
  
  def buy(self, bike, store):
    self.owned.append(bike)
    self.fund -= store.inventory[bike]["price"]
    print self.name + " bought " + bike.model + " and has $" + str(self.fund) + " left in his/her fund!"
    
  def print_affordable(self, store): 
    print customer.name + " has $" + str(customer.fund) + " and can buy the following from " + store.name + ":"
    for bike in store.inventory:
      if customer.fund >= store.inventory[bike]["price"]:
        self.affordable.append(bike)
        print bike.model + " for $" + str(store.inventory[bike]["price"])
    print ""
    
customerA = Customer("Aaron", 500)
customerB = Customer("Becky", 800)
customerC = Customer("Chris", 2000)
customer_list = [customerA, customerB, customerC]
      
#Purchase function defines changes to 'Bike_shop' and 'Customer' objects when a customer buys a bike
def purchase(customer, bike, store):
  customer.buy(bike, store)
  store.sell(bike)

def random_purchase_all(store):
  for customer in customer_list:
    available = []
    for bike in customer.affordable:
      if store.inventory[bike]["stock"] > 0:
        available.append(bike)
    x = random.choice(available)
    purchase(customer, x, store)

if __name__ == "__main__":
  for customer in customer_list:
    customer.print_affordable(jareds)
  
  jareds.print_inventory()
  
  random_purchase_all(jareds)
  
  jareds.print_inventory()
  
  jareds.print_profit()
  