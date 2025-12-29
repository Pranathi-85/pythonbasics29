#Q1 -polymorphism

class Animal:
    def make_sound(self):
        print("sound")
class Dog(Animal):
    def make_sound(self):
        print("Dog sound")
class Cat(Animal):
    def make_sound(self):
        print("Cat sound")
class Cow(Animal):
    def make_sound(self):
        print("Cow sound")
obj=Animal()
dog=Dog()
cat=Cat()
cow=Cow()
dog.make_sound()
cat.make_sound()
cow.make_sound()
obj.make_sound()


#Q2-Duck Typing
class Car:
    def start(self):
        return("dugh dugh")
class Computer:
    def start(self):
        return "pop pop"
        #print("pop pop")
class washing_machine:
    def start(self):
        return("garr garr")
def operate(device):
    print(device.start())

#obj=Car()
#obj1=Computer()
#obj2=washing_machine()
#obj.start()
#obj1.start()
#obj2.start()
operate(Car())
operate(Computer())
operate(washing_machine())
#operate(obj)
#operate(obj1)
#operate(obj2)

#Q3-Polymorphism
# Create a Vector class that supports:
#+ operator add coordinates
#== operator compare equality
#Show how operator overloading gives natural polymorphism to user-defined classes.


class vector:
  def __init__(self,x,y):
      self.x=x
      self.y=y
  def __add__(self,obj2):
      return self.x + obj2.x ,self.y + obj2.y
  def __eq__(self,obj2):
      return self.x==obj2.x and self.y==obj2.y
v1=vector(1,2)
v2=vector(3,4)

print(v1 + v2)
print(v1==v2)


#Q4-Polymorphism
#Create a base class Transport with move() and derived classes Bus and Bike that override it
# but also call the parent implementation using super().
#Show the combination of reuse custom behavior.

class Transport:
     def move(self):
         print("Transport means going from one place to another")
class Bus(Transport):
    def move(self):
        super().move()
        print("bus colour is red")
class Bike(Transport):
    def move(self):
        super().move()
        print("bike colour is black")

#t1=Transport()
#bus=Bus()
#bike=Bike()
Bus().move()
Bike().move()
#bus.move()
#bike.move()

#Q6-Polymorphism
class payment:
    def process(self,amount):
        print(f"processing amount of {amount}")
class creditcardpayment(payment):
    def process(self,amount,card_type):
        print(f"processing {card_type} payment of {amount}")

p1=payment()
c1=creditcardpayment()

p1.process(1000)
c1.process(1000,"Visa")

#Q7-Duck Typing
class sorter:
    def change(self,strategy):
        strategy.logic()
class BS:
    def logic(self):
        print("Best Start")
class MS:
    def logic(self):
        print("Must Start")
class QS:
    def logic(self):
        print("Quick Start")
s=sorter()
obj1=BS()
obj2=MS()
obj3=QS()
s.change(obj1)
s.change(obj2)
s.change(obj3)



#8-Duck Typing
class Circle:
    def draw(self):
        print("it is circle")
class square:
    def draw(self):
        print("it is square")
class rectangle:
    def draw(self):
        print("it is rectangle")
def draw(shape):
    shape.draw()
class car:
    def draw(self):
        print("it is a car")
c1=Circle()
s1=square()
r1=rectangle()
car1=car()
c1.draw()
s1.draw()
r1.draw()
car1.draw()

#Q9-Polymorphism
from abc import ABC ,abstractmethod
class notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Email_notification(notification):
    def send(self):
        print("sendog Email")
class SMS_notification(notification):
    def send(self):
        print("sending SMS")
class Push_notification(notification):
    def send(self):
        print("sending push")
obj=[Email_notification(),SMS_notification(),Push_notification()]
for n in obj:
    n.send()

#Q10-Polymorphism
class Account:
    def withdraw(self,amount):
        print(f"[Account] withdrawing {amount}")
class Saving_Account(Account):
    def withdraw(self,amount):
        super().withdraw(amount)
        print(f"[Saving_Account] withdrawing {amount}")
class premium_saving_account(Account):
    def withdraw(self,amount):
        super().withdraw(amount)
        print(f"[premium_saving_account] withdrawing completed with premium benefits")
accounts=[Account(),Saving_Account(),premium_saving_account()]
for acc in accounts:
    acc.withdraw(10000)












