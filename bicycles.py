class Bike(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost

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
    print self.name + " has $" + str(self.fund) + " and can buy the following from " + store.name + ":"
    for bike in store.inventory:
      if self.fund >= store.inventory[bike]["price"]:
        self.affordable.append(bike)
        print bike.model + " for $" + str(store.inventory[bike]["price"])
    print ""