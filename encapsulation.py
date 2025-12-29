#getter method
class A:
    def __init__(self,a):
        self.a=a
        self._b=10
        self.__c=20
    def method(self):
        return self.__c
obj=A(30)
print(obj.method())

#setter method
class A:
    def __init__(self,a):
        self.a=a
        self._b=10
        self.__c=20

    @property
    def change(self):
        return self.__c
    @change.setter
    def change(self,new):
        self.__c=new

obj=A(30)
obj.change=40
print(obj.change)



# implement encapsulation,
# inheritance, polymorphism in a single program
class RBI:
    def __init__(self,name):
        self.name=name
        self.type="savings"
        self._balance=0
        self.__pin=1234
    def deposit(self,amount):
        self._balance=self._balance+amount
    @property
    def atmpin(self):
        return self.__pin
    @atmpin.setter
    def atmpin(self,value):
        self.__pin=value
class Axis(RBI):
    def __init__(self,name):
        super().__init__(name)
        self.tax=100
    def show_balance(self):
        return self._balance
    def deposit(self,amount):
        self._balance=(self._balance+amount)-self.tax
a1=Axis("Keerthi")
print(a1.show_balance())
print(a1.atmpin)
a1.atmpin=4567
print(a1.atmpin)
a1.deposit(1000)
print(a1.show_balance())

#1. Create a BankAccount class that stores:
#account number
#balance (should not be directly modifiable)
#You must:
#1. Make the balance attribute inaccessible from outside.
#2. Provide functions to deposit/withdraw that validate the amount.
#3. Prevent withdrawal if balance becomes negative.
#4. Show what happens if someone tries to modify balance directly and why
#encapsulation prevents it.

class BankAccount:
    def __init__(self,name,acc_number):
        self.name=name
        self.Acc_number=acc_number
        self.__balance=0
    @property
    def change(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance=self.__balance-amount
            return self.__balance
        return ("Insufficient Balance")
    def show_balance(self):
        return self.__balance
c1=BankAccount("pranathi",2014896754)
c1.deposit(10000)
print(c1.show_balance())
c1.withdraw(5000)
print(c1.show_balance())
print(c1.change)


#2. Design a Student class where marks:
#should always be between 0 and 100
#should never be set directly
#Enable updating marks only through a controlled method that performs range checks.
#Demonstrate:
#trying to assign marks manually
#why encapsulation protects invalid states


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def update_marks(self,new_marks):
        if 0<new_marks<=100:
            self.__marks=new_marks
            return self.__marks
        return "Invalid Marks"
stu1=Student("pranathi",80)
print(stu1.get_marks())
print(stu1.update_marks(100))

#3. Create a Securefile class that:
#stores content privately
#provides a method read (passwardi)
#refuses access if the password is incorrect
#logs an "Unauthorized attempt" internally (cannot be accessed from outside)

class Securefile:
    def __init__(self,content,password,log):
        self.__content=content
        self.__password=password
        self.__log=log
    def read(self,user_password):
        if user_password==self.__password:
            return self.__content
        return "Unauthorized attempt"



#4.Design an Employee class where:salary is hidden outsiders cannot read salary directly
#use getter method that logs each access attempt
#provide a method to update salary but only if the new salary is higher (prevent
#accidental downgrade)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        self.__access_attempt=0
    @property
    def getter(self):
        self.__access_attempt+=1
        return self.__salary
    def update_salary(self,new_salary):
        if self.__salary<new_salary:
            self.__salary=new_salary
            return self.__salary
        return "cannot update"
    #@property
    def getter2(self):
        return self.__access_attempt
emp1=Employee("charan",100000)
print(emp1.getter)
print(emp1.getter)

print(emp1.update_salary(150000))
print(emp1.getter2())


#5. Create a Product class where:
#price cannot be negative
#discount cannot exceed 70%
#internal final price calculation should not be directly exposed
#Provide only one public method get_final price().

class Product:
    def __init__(self,price,discount):
        self.__price=price
        self.__discount=discount
    def __calculation(self):
        if 0 < self.__discount < 70:
            final_price=self.__price-(self.__price*self.__discount/100)
            return  final_price
        return "discount cannot be exceed"
    def get_final_price(self):
        return self.__calculation()
    def determine(self):
        if self.__price>0:
            return self.__price
        return "Negative"

p1=Product(1000,80)
print(p1.get_final_price())



#6. Create a Character class with: private health
#methods to damage (points) and heal (points)
#health cannot drop below 0 or exceed max limit
#expose only current health through a read-only getter















#7. Create: An Engine class with private state like temperature
#A Car class that uses an Engine but should:
#Not allow users to manipulate engine temperature
#Only expose methods like start_car() or cool_engine()
#Demonstrate why giving direct engine access is dangerous.









#8. Create a shoppingCart class where: items are stored privately
#users cannot directly modify item list
#only add/remove methods are allowed
#provide a method to get a safe copy of the cart items
# (not direct reference to internal

class shoppingCart:
    def __init__(self):
        self.__items=[]
    def add_items(self,items):
        if items in self.__items:
            return f"{items} already in the list"
        self.__items.append(items)
        return self.__items

    def remove_items(self,item):
        if item in self.__items:
            self.__items.remove(item)
    def save_copy(self):
        return self.__items.copy()  #here if any outsider want to modify the list items copy can add that items but the real list can be safe
obj=shoppingCart()
print(obj.add_items("laptop"))
print(obj.add_items("mouse"))
print(obj.add_items("keyboard"))
print(obj.add_items("keyboard"))
print(obj.save_copy())
lst=obj.save_copy()
lst.append("rotter")
print(lst)
print(obj.save_copy())


#9. Implement a class incorrectly first:
#Attendance stored in a list
#Exposed directly so any outside code can modify it
#Then redesign properly:
#Make attendance private
#Provide controlled methods for marking attendance only
#Explain the difference.











#10. Create a class using @property and setter for a private attribute.
#Then:
#1. Show correct usage
#2. Show how forgetting to use underscore prefix breaks encapsulation
#3. Show what happens if you implement a setter without validation
#Focus: Python-specific encapsulation pitfalls, misuse of properties.





