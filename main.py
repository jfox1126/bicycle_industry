import random

from bicycles import Bike #Bike class takes a model, weight, and cost as arguments
from bicycles import Bike_shop #Bike_shop class takes a name, profit margin, and inventory {bike object: # in stock}
from bicycles import Customer #Customer class takes a name and fund with which it can buy bikes

#Define a set of bikes
model1 = Bike("Model1", 30, 400)
model2 = Bike("Model2", 25, 500)
model3 = Bike("Model3", 20, 600)
model4 = Bike("Model4", 20, 750)
model5 = Bike("Model5", 18, 1000)
model6 = Bike("Model6", 16, 1500)
bike_list = [model1, model2, model3, model4, model5, model6]
  
#Define a bike shop and starting inventory
inventory2 = {
  model1: 1,
  model2: 2,
  model3: 3,
  model4: 3,
  model5: 2,
  model6: 1,
}

jareds = Bike_shop("Jared's", .2, inventory2)
 
#Define several customers
customerA = Customer("Aaron", 500)
customerB = Customer("Becky", 800)
customerC = Customer("Chris", 2000)
customer_list = [customerA, customerB, customerC]
      
#Purchase function causes customer to gain a bike and lose funds; bike_shop to lose inventory and gain profit
def purchase(customer, bike, store):
  customer.buy(bike, store)
  store.sell(bike)

def random_purchase_all(store):
  """Has each cutomer in customer_list buy a bike that is both affordable and in stock"""
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
  