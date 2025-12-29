#1. Design a banking system with:
#• An abstract base class Account with deposit(), withdraw(),
#calculate_interest().
#• Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
#• Each account must:
# Encapsulate balance (private)
# Provide controlled access through properties
# Override interest calculation differently
# Include a static method to validate amount.
# Include a class method to update bank-wide interest policies.

from abc import ABC , abstractmethod
class Account(ABC):
    interest_rate={"SA":0.03,"CA":0.15,"FD":0.50}

    def __init__(self,name,balance=0):
        self.name=name
        self.__balance=balance

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
    @property
    def balance(self):
        return self.__balance

    def set_balance(self,amount):
        self.__balance=amount
    @staticmethod
    def validate_amount(amount):
        if amount<=0:
            return "Account should have some amount"
    @classmethod
    def update_interest(cls,ACC_type,rate):
        cls.interest_rate[ACC_type]=rate

class saving_account(Account):
    def deposit(self,amount):
        self.set_balance(self.balance+amount)
    def withdraw(self,amount):
        if self.balance<amount:
            return "insufficient balance"
        self.set_balance(self.balance-amount)
    def calculate_interest(self):
        rate=Account.interest_rate["SA"]
        return self.balance*rate

class Current_Account(Account):
    def deposit(self,amount):
        self.set_balance(self.balance+amount)
    def withdraw(self,amount):
        self.validate_amount(amount)
        if self.balance<amount:
            return "insufficient balance"
        self.set_balance(self.balance - amount)
    def calculate_interest(self):
        rate=Account.interest_rate["CA"]
        return self.balance*rate

class Fixed_deposit_Account(Account):
    def __init__(self,name,balance,year):
        super().__init__(name,balance)
        self.year=year
    def deposit(self,amount):
        return "cannot deposit after opening FD"
    def withdraw(self,amount):
        return "cannot withdraw before date"
    def calculate_interest(self):
        rate=Account.interest_rate["FD"]
        return self.balance*rate*self.year

s=saving_account("pranathi",1000)
s.deposit(200)
s.withdraw(300)
print(s.balance)
print(s.calculate_interest())

#2. Build:
# Vehicle base class
# Car, Bike, Auto subclasses
# A Driver class that contains a Vehicle
# A Ride class that:
# Calculates fare differently depending on the type of vehicle (polymorphism)
# Stores driver + vehicle combination
# Protects internal fare formula through encapsulation
#Also:
# Use __str__ to print readable ride summaries.



class vehicle():
    def __init__(self, model):
        self.model = model


    def calculate_fare(self):
        print("cannot allowed")

class Car(vehicle):
    def calculate_fare(self):
        return "amount is $150"


class Bike(vehicle):
    def calculate_fare(self):
        return "amount is 75"


class Auto(vehicle):
    def calculate_fare(self):
        return "amount is 90"


class Driver(vehicle):
    def __init__(self, driver_name, vehicle):
        self.driver_name = driver_name
        self.vehicle = vehicle


class Ride:
    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.__fare = self.__calc_fare()

    def __calc_fare(self):
        return self.driver_name.vehicle.calculate_fare()

    @property
    def fare(self):
        return self.__fare

    def __str__(self):
        return (f"Driver Name: {self.driver_name.driver_name}\n"
                f"Vehicle Name: {self.driver_name.vehicle.model}\n"
                f"Fare: {self.fare}\n")

#
car = Car("KIA")
bike = Bike("Honda")
auto = Auto("Mahendra")


d1 = Driver("Balu", car)
d2 = Driver("Raju", bike)
d3 = Driver("Sai", auto)

# ---- Create rides ----
r1 = Ride(d1)
r2 = Ride(d2)
r3 = Ride(d3)

print(r1)
print(r2)
print(r3)


#3. Create:
#  Abstract class PaymentMethod with pay(), validate()
# Subclasses: CardPayment, WalletPayment, UPIPayment
# Encapsulate user balance
# Use @property to control reading available funds
# Overload + operator to combine two payment methods into “split payment”
# Demonstrate polymorphism through a checkout loop.

from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def validate(self):
        pass
    def __add__(self,other):
        return SplitPaymentMethod(self,other)
class CardPayment(PaymentMethod):
    def  __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def pay(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            return f"paid {amount} using card"
        return "Insufficient balance"
    def validate(self):
        return "card validated"
class WalletPayment(PaymentMethod):
    def  __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def pay(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            return f"paid {amount} using Wallet"
        return "Insufficient balance"
    def validate(self):
        return "wallet validated"
class UPIPayment(PaymentMethod):
    def  __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    def pay(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            return f"paid {amount} using UPI"
        return "Insufficient balance"
    def validate(self):
        return "UPI validated"
class SplitPaymentMethod:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def pay(self,amount):
        half=amount/2
        r1=self.p1.pay(half)
        r2=self.p2.pay(half)
        return f"{r1} {r2}"

card=CardPayment(300)
wallet= WalletPayment(200)

c1=card + wallet
print(c1.pay(100))
print(card.validate())
print(wallet.validate())





#4. Create classes:
# Person → base
# MedicalStaff(Person)
# Doctor(MedicalStaff)
# Surgeon(Doctor)
#Requirements:
# Hide sensitive data (e.g., salary, patient notes)
# Abstract method perform_duty()
# Each level overrides the method with more specific behavior
# Use super() to chain constructor calls
#Demonstrate consistency across hierarchy

from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def perform_duty(self):
        pass
class Medical_staff(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.__salary=salary
    def perform_duty(self):
        return "medical staff helps patients "
class Doctor(Medical_staff):
    def __init__(self,name,salary,patient_notes):
        super().__init__(name,salary)
        self.__patient_notes=patient_notes
    def perform_duty(self):
        return "Doctors helps patients for their recovery"
class Surgeon(Doctor):
    def __init__(self,name,salary,patient_notes,speciality):
        super().__init__(name,salary,patient_notes)
        self.speciality=speciality
    def perform_duty(self):
        return "Surgeon  helps patients for their operations "
ms=Medical_staff("pranathi",25000)
dr=Doctor("raghu","100000", "drink more water")
sn=Surgeon("lakshmi",200000,"critical cases","neurologist")

print(ms.perform_duty())
print(dr.perform_duty())
print(sn.perform_duty())


#5. Classes:
# User
# Instructor(User)
# Student(User)
# TeachingAssistant(Student, Instructor)
#Requirements:
# Track course assignments privately
# Ensure TAs override submit_work() and grade_work()
# Print MRO and explain how Python resolves conflicts

class User:
    def __init__(self,name):
        self.name=name
class Instructor(User):
    def __init__(self,name):
        self.name=name
        self.__assignments=[]
    def add_assignments(self,work):
        self.__assignments.append(work)
    @property
    def get_asssignments(self):
        return self.__assignments
class student(User):
    def submit_work(self,work):
        return f"{self.name} completed {work}"
class Teaching_Assistant(student,Instructor):
    def __init__(self,name):
        Instructor.__init__(self,name)
        student.__init__(self,name)
    def submit_work(self,work):
        return f"{self.name} submitted {work} to TA"
    def grade(self,work,grade):
        return f"{self.name} completed {work} with {grade}"

teacher=Instructor("sravani")
stu=student("sravanthi")
TA=Teaching_Assistant("raghu")

teacher.add_assignments("CN Assignment")
stu.submit_work("CN Assignment")
TA.submit_work("CN Assignment")
TA.grade("CN Assignment",9.0)

print(stu.submit_work("CN Assignment"))
print(Teaching_Assistant.__mro__)
print(Instructor.__mro__)
print(student.__mro__)


#6. Create:
# Product class with private price and quantity
# Warehouse class containing multiple products
# Overload:
# + to merge warehouses
# len() to return number of unique products
# in operator to check if product exists
# Provide class method to track total warehouses created

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.__price = price
        self.__qty = qty


class Warehouse:
    total = 0

    def __init__(self):
        Warehouse.total += 1
        self.products = []

    def add_product(self, p):
        self.products.append(p)

    def __add__(self, other):

        w = self.products + other.products
        return w

    def __len__(self):
        return len(self.products)

    def __contains__(self, name):
        return name in self.products

    @classmethod
    def total_warehouses(cls):
        return cls.total

p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 2)


w1 = Warehouse()
w2 = Warehouse()


w1.add_product(p1)
w2.add_product(p2)

w3 = w1 + w2


print(len(w3))
print("Book" in w2)
print(Warehouse.total_warehouses())

#7 Design:
# Abstract class MediaFile with play(), stop()
# Subclasses: MP3File, MP4File, WAVFile
# Private file path validation done internally
# A function start_player(media) that works with ANY object that has play()
#(duck typing)
#Demonstrate mixing true polymorphism + duck typing.


from abc import ABC ,abstractmethod

class MediaFile(ABC):
    def __init__(self,path):
        self.path=path
        self.__validate()
    def __validate(self):
        return "invalid path"
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3File(MediaFile):
    def play(self):
        print("MP3File is playing")
    def stop(self):
        print ("MP3File is stopped")

class MP4File(MediaFile):
    def play(self):
        print("MP4File is playing")
    def stop(self):
        print("MP4File is stopped")

class WAVFile(MediaFile):
    def play(self):
        print ("WAVFile is playing")
    def stop(self):
        print ("WAVFile is stopped")

def media_player(media):
    media.play()
    media.stop()
mp3=MP3File("movie.mp3")
mp4=MP4File("song.mp4")
wav=WAVFile("sound.wav")

media_player(mp3)
media_player(mp4)
media_player(wav)


#8. Create:
# Abstract class StatementFormatter
# Subclasses: PDFFormatter, JSONFormatter, TextFormatter
# Overload __call__() so that formatters can be used like functions
# Overload __repr__ for debugging
# Demonstrate polymorphic behavior in a reporting pipeline

from abc import ABC ,abstractmethod
class StatementFormatter(ABC):
    @abstractmethod
    def start_formatter(self):
        pass
    def __call__(self):
        return self.start_formatter()
    def __repr__(self):
        return self._class.name_
class PDFFormatter(StatementFormatter):
    def start_formatter(self):
        return "This is a PDF report."
class JSONFormatter(StatementFormatter):
    def start_formatter(self):
        return '{"report": "JSON formatted report"}'
class TextFormatter(StatementFormatter):
    def start_formatter(self):
        return "This is a simple text report."
def reporting_pipeline(formatters):
    for i in formatters:
        print("using",i)
        print(i())

formatters=[PDFFormatter(),JSONFormatter(),TextFormatter()]
reporting_pipeline(formatters)


#9. Classes:
#LightDevice
# SecurityDevice
# SmartCamera(LightDevice, SecurityDevice)
#Requirements:
# Resolve method conflicts using MRO
# Encapsulate internal camera logs
# SmartCamera overrides both parents’ behaviors
# Use super() responsibly in multiple inheritance

class LightDevice:
    def activate(self):
        print("turn on")
    def deactivate(self):
        print("turn off")
class SecurityDevice:
    def activate(self):
        print("Armed Stay")
    def deactivate(self):
        print("Armed Away")
class SmartCamera(LightDevice, SecurityDevice) :
    def __init__(self):
        self.__log=[]
    def activate(self):
        super().activate()
    def deactivate(self):
        super().deactivate()



scam=SmartCamera()
scam.activate()
scam.deactivate()

print(SmartCamera.__mro__)

#10. Create:
# Abstract class MenuItem with get_price()
# Subclasses: Pizza, Burger, Drink
# Order class containing a list of items (composition)
# Encapsulate the list internally
# Override methods to apply custom pricing logic for each food type

from abc import ABC ,abstractmethod
class MenuItem(ABC):
    @abstractmethod
    def get_price(self):
        pass
class Pizza(MenuItem):
    def __init__(self,price):
        self.price=price
    def get_price(self):
        return f"{self.price}"
class Burger(MenuItem):
    def __init__(self,price):
        self.price=price
    def get_price(self):
        return f"{self.price}"
class Drink(MenuItem):
    def __init__(self,price):
        self.price=price
    def get_price(self):
        return f"{self.price}"
class Order:
    def __init__(self):
        self.__item=[]
    def add_items(self,item):
        self.__item.append(item)
        return f"{item.get_price()}"

pizza=Pizza(250)
burger=Burger(200)
drink=Drink(20)
order=Order()
     
print(order.add_items(pizza))
print(order.add_items(burger))
print(order.add_items(drink))


#11. Create:
# Class Applicant with private skills list
# Overload:
# + to add skill
# - to remove skill
# == to compare applicants who have identical skill sets
# Use inheritance to create ExperiencedApplicant with additional fields

class Applicant:
    def __init__(self,name):
        self.name=name
        self.__skills=[]
    def __add__(self,skill):
        self.__skills.append(skill)
    def __sub__(self,skill):
        if skill in self.__skills:
            self.__skills.remove(skill)
    def __eq__(self,other):
        return self.__skills==other.__skills
 
    @property
    def get_skills(self):
        return self.__skills
class ExperienceApplicant(Applicant):
    def __init__(self,name,experience):
        super().__init__(name)
        self.experience=experience

p1=Applicant("pranathi")
p1 + "SQL"
p1 + "ui/ux"

p2=Applicant("charan")
p2 + "Django"
p2 + "python"
p2 - "Django"

exp=ExperienceApplicant("hemanth",5)
exp + "java"

print(p1.get_skills)
print(p2.get_skills)
print(p1==p2)
print(exp.experience,exp.get_skills)


#12. Create:
# Character → base class
#Warrior, Archer, Mage subclasses
#Each subclass:
# Overrides attack()
# Encapsulates health with @property
#Prevents negative HP
# Uses class attributes for shared attributes (e.g., stamina_cost)

class Character:
    stamina_cost=0
    def __init__(self,name,health=100):
        self.name=name
        self.__health=health

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,value):
        if value<0:
            self.__health=0
        else:
            self.__health=value


class Warrior(Character):
    def attack(self,weapon):
        self.health=self.health-Character.stamina_cost
        return f"Warrior attacking with {weapon}"
class Archer(Character) :
    def attack(self,weapon):
        self.health = self.health -Character.stamina_cost
        return f"Archer attacking with {weapon}"
class Mage(Character):
    def attack(self,weapon):
        self.health = self.health - Character.stamina_cost
        return f"MAge attacking with {weapon}"
w1=Warrior("pranathi")
print(w1.attack("knife"))
print(w1.health)


#13. Build:
# Transport abstract class
# Subclasses: Taxi, Bus, Train
# Each implements:
# calculate_fare() differently
# Use static method to validate distance
# Encapsulate fare state
# Add class method to update government tax slab

from abc import ABC,abstractmethod
class Transport(ABC):
    gov_tax=20
    def __init__(self,price,distance):
        self.price=price
        self.distance=distance
        self.__fare=0
    @abstractmethod
    def calculate_fare(self):
        pass
    @property
    def fare(self):
        return self.__fare
    @staticmethod
    def valid_distance(distance):
        if distance>=0:
            return "valid"

    @classmethod
    def change_tax(cls,new_tax):
        cls.gov_tax=new_tax

class Taxi(Transport):
    def calculate_fare(self):
        return self.distance+self.price*(0.8)+self.gov_tax
class Bus(Transport):
    def calculate_fare(self):
        return self.distance+self.price+self.gov_tax
class Train(Transport):
    def calculate_fare(self):
        return self.distance+self.price*(0.5)+self.gov_tax


b1=Bus(50,30)
t1=Taxi(100,30)
tr1=Train(90,150)

print(b1.calculate_fare())
print(t1.calculate_fare())
print(tr1.calculate_fare())

#14. Design:
# Abstract class Model with train(), predict()
# Implement LinearRegressionModel and DecisionTreeModel(just print or
#write a logic, focus on calling and concept)
# A Pipeline class that:
# Accepts any model
# Uses composition to chain transformations
# Overloads __call__() to run predictions
# Encapsulates internal steps






#15.
#Classes:
#• User
#Create a mini version of Amazon with:
#• Product
#• Seller(User)
#• Buyer(User)
#• Order
#• Cart
#Requirements (must use all OOP concepts):
#>Inheritance: Seller and Buyer extend User
#>Encapsulation: protect internal cart list, user password
#>Abstraction: base class User defines abstract get_role()
#>Polymorphism: different users behave differently in checkout
#>Composition: Buyer “has” a Cart
#>Operator overloading:
#• + to add product to Cart
#• - to remove product
#>Properties: validate product price
#>Class methods: tracking total users
#>Static methods: validating product IDs
#>__str__ for readable summaries
#>MRO behavior when Buyer inherits from multiple mixins (e.g., RewardsMixin)"""
import sys
import sys
from abc import ABC, abstractmethod

# ---------------- ABSTRACT CLASS FIRST ----------------
class User(ABC):
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.__password = password     # encapsulation
        User.total_users += 1

    @abstractmethod
    def get_role(self):
        pass

    @classmethod
    def count(cls):
        return cls.total_users

    @staticmethod
    def validate_id(pid):
        return pid > 0


# ------------------------------------------------------


# Product with private price + property
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price


# Cart (composition + operator overloading)
class Cart:
    def __init__(self):
        self.__items = []    # private list

    def add_items(self, product):
        return self.__items.append(product)


    def sub_items(self, product):
        return self.__items.remove(product)

    def get_items(self):
        return self.__items


# Seller inherits User (Inheritance)
class Seller(User):
    def get_role(self):
        return "Seller"

    def checkout(self):     # Polymorphism
        return "Seller cannot checkout"


# Buyer inherits User + HAS a Cart (Composition)
class Buyer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.cart = Cart()

    def get_role(self):
        return "Buyer"

    def checkout(self):     # Polymorphism
        return "Buyer checkout successful"





class Order:
    def __str__(self):
        return "Order Summary"
p1 = Product("Pen", 10)
p2 = Product("Book", 50)

b = Buyer("Ram", "123")
s = Seller("Ravi", "456")

b.cart.add_items(p1)
b.cart.add_items(p2)

print(b.checkout())
print(s.checkout())
print(User.count())
 
