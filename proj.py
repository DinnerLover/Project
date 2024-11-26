class Donut:
    def __init__(self, name, price, shop):
        self.name = name
        self.price = price
        self.shop = shop
    def updateShop(self, shop):
        self.shop = shop
    def buyFromShop(self):
        if self.shop == 0: # if there is no items available
            # raise not item exception
            pass
        self.shop -= 1
class Cafe:
    def __init__(self):
        self.amount = 0
        self.Donuts = []
    def addDonuts(self, donut):
        self.Donuts.append(donut)
    def showDonuts(self):
        print("_________\nDonuts in shop\n_________")
        for donut in self.Donuts:
            if donut.shop == 0:
                self.Donuts.remove(donut)
        for donut in self.Donuts:
            print(donut.name + ": " "Rp.", donut.price) 
        print("__________\n")
    def addCash(self, money):
        self.amount = self.amount + money
    def buyDonut(self, donut):
        if self.amount < donut.price:
            print("Sorry, but you don't have enough cash for that.") 
        else:
            self.amount -= donut.price
            donut.buyFromShop()
            print(f"{donut.name} has been purchased!")
            print(f"You have {self.amount} cash left.")

    def containsDonuts(self, wanted):
        ret = False
        for donut in self.Donuts:
            if donut.name == wanted:
                ret = True
                break
        return ret
    def getDonut(self, wanted):
        ret = None
        for donut in self.Donuts:
            if donut.name == wanted:
                ret = donut
                break
        return ret
    def insertAmountForDonut(self, donut):
        price = donut.price
        while self.amount < price:
                self.amount = self.amount + float(input("It is Rp." + str(price - self.amount) + ", how much would you like to pay? "))
    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0
            print("Have a nice day!\n")
def donut():
    shop = Cafe()
    Donut1 = Donut("Plain", 8000, 6)
    Donut2 = Donut("Chocolate", 8500, 4)
    Donut3 = Donut("PB&C", 12500, 3)
    Donut4 = Donut("Cream Cheese", 15000, 2)
    Donut5 = Donut("Dubai Choco", 180000, 3)
    Donut6 = Donut("Strawberry", 9000, 6)
    Donut7 = Donut("Double Choco", 9800, 4)
    shop.addDonuts(Donut1)
    shop.addDonuts(Donut2)
    shop.addDonuts(Donut3)
    shop.addDonuts(Donut4)
    shop.addDonuts(Donut5)
    shop.addDonuts(Donut6)
    shop.addDonuts(Donut7)
    print("_______CAFE WHATSITSNAME_______\n")
    continueToBuy = True
    while continueToBuy == True:
        shop.showDonuts()
        selected = input("Which donut do you want")
        if shop.containsDonuts(selected):
            donut = shop.getDonut(selected)

            shop.insertAmountForDonut(donut)
            shop.buyDonut(donut)

            a = input("Want anything else? (y/n): ")
            if a == "n":
                continueToBuy = False
                shop.checkRefund()
            else:
                continue
        else:
            print("Sorry about that, but the donut you're trying to buy is currently unavailable. Choose another donut.")
            continue
donut()