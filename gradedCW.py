# !! : more comments please
#Problem 1
class Dog:
    def __init__(self,name,breed,color,gender):
        self.name=name
        self.breed=breed
        self.color=color
        self.gender=gender
    def printAttributes(self):
        print(f"{self.name}, {self.breed},{self.color},{self.gender}") # !! : use strinf formatting to take advantage of f strings 

def problem1():
    myDog= Dog("Santana","Golden Retriever","Brown","Female")
    myDog.printAttributes()

#Problem 2
def problem2():
    userInput= input("Enter a word: ")
    while(userInput!="q"): # !! : quits with the equal sign
         userInput= input("Try Again: ")

#Problem 3
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def printOriginal(self):
        print(f"{self.name},{self.price},{self.quantity}")
    def changeName(self,newname):
            self.name = newname
            print(f"The new product name is {self.name}")
    def changeNameandProduct(self,newname,newprice):
        self.name = newname
        self.price = newprice
        print(f"The new product name is {self.name} and the price has been updated to $ {self.price}")
    def changeAllAttributes(self,newname,newprice,newquantity):
        self.name = newname
        self.price = newprice
        self.quantity = newquantity
        print(f"The new product name is {self.name}" 
              f"The price has been updated to $ {self.price}\n" 
              f"The quantity has been updated to  {self.quantity}")
def problem3():
    newProduct = Product("Ninentdo 64",8.99,2)
    newProduct.printOriginal()
    newProduct.changeName("SegaDreamCast")
    newProduct.changeNameandProduct("SegaDreamcast",99)
    newProduct.changeAllAttributes("SegaDreamCast",99,4)

def main():
    problem1()
    problem2()
    problem3()

main()