""" Created by Coleman Holmes """

""" class definition """
class VendingMachine:
  def __init__(self):
    self.selection=0
    self.balance=0
    self.inventory = {
      1 : { "name": "Chips",
            "price": 2
            },
      2 : { "name": "Coke",
            "price": 1
             },
      3 : { "name": "Popcorn",
            "price": 3
             },
    }

    """ This method prints the menu and then calls the inputMoney method """
  def printMenu(self):
    print("\n\n\n")
    for key,item in self.inventory.items():
      print(key,". ",item["name"], " $",item["price"])
    selection=input("Please enter the number of your selection:\n")
    try:
      self.selection=int(selection)
      self.inputMoney()
    except:
      while not selection.isdigit():
        selection=input("Please enter a number:\n")
      self.selection=int(selection)
      self.inputMoney()

""" This method will update the current balance for the user and then call the balanceCheck method """
  def inputMoney(self):
    item = self.inventory[self.selection]
    print("Please insert $", item["price"],"for",item["name"])
    money=input()
    try:
      self.balance+=int(money)
    except:
      while not money.isdigit():
        money=input("Please enter a number:\n")
      self.balance+=int(money)
    self.balanceCheck()

""" The balanceCheck method will compare the price of the selection to the inputed money from the user """
  def balanceCheck(self):
    item = self.inventory[self.selection]
    if self.balance==item["price"]:
      print("Dispensing decilcious snack!")
    if self.balance>item["price"]:
      change=self.balance-item["price"]
      print("Dispensing decilcious snack and $",change,"in change")
    if self.balance<item["price"]:
      while self.balance<item["price"]:
        print("Please insert $",item["price"]-self.balance, "more:")
        add=input()
        try:
          self.balance+=int(add)
        except:
          while not add.isdigit():
            add=input("Please enter a number:\n")
          self.balance+=int(add)
      if self.balance==item["price"]:
        print("Dispensing decilcious snack!")
      if self.balance>item["price"]:
        change=self.balance-item["price"]
        print("Dispensing decilcious snack and $",change,"in change")
    self.clearFields()

""" This method will clear all the variables so the program may automatically rerun itself """
  def clearFields(self):
    self.selection=0
    self.balance=0

""" This is the object that is an instance of the VendingMachine class """
machine=VendingMachine()
loop=1
while loop==1:
  machine.printMenu()