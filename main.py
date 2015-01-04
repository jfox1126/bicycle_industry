import random

from bicycles import Wheel #Wheels class takes a model, weight, and production cost
from bicycles import Frame #Frame class takes a material, weight, and produciton cost
from bicycles import Bike #Bike class takes a model, wheel type, and frame material
from bicycles import Bike_shop #Bike_shop class takes a name, profit margin, and inventory {bike object: # in stock}
from bicycles import Customer #Customer class takes a name and fund with which it can buy bikes

#Define a set of bike parts
wheelA = Wheel("ModelA", 4, 50)
wheelB = Wheel("ModelB", 3, 100)
wheelC = Wheel("ModelC", 2, 200)

aluminum_frame = Frame("aluminum", 15, 300)
steel_frame = Frame("steel", 20, 600)
carbon_frame = Frame("carbon", 10, 900)

#Define a set of bikes with different parts
model1 = Bike("Model1", wheelA, aluminum_frame)
model2 = Bike("Model2", wheelB, aluminum_frame)
model3 = Bike("Model3", wheelA, steel_frame)
model4 = Bike("Model4", wheelC, steel_frame)
model5 = Bike("Model5", wheelB, carbon_frame)
model6 = Bike("Model6", wheelC, carbon_frame)
bike_list = [model1, model2, model3, model4, model5, model6]
  
#Define a bike shop and starting inventory
jareds_inventory = {
  model1: 1,
  model2: 2,
  model3: 3,
  model4: 3,
  model5: 2,
  model6: 1,
}

jareds = Bike_shop("Jared's", .2, jareds_inventory)
 
#Define several customers
customerA = Customer("Aaron", 500)
customerB = Customer("Becky", 900)
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

#To run program from command line
if __name__ == "__main__":
  for customer in customer_list:
    customer.print_affordable(jareds)
  
  jareds.print_inventory()
  
  random_purchase_all(jareds)
  
  jareds.print_inventory()
  
  jareds.print_profit()
  