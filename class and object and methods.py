#creating a class
class A:
    x=5
print(A)
#creating an object
p1=A()
print(p1.x)
##creating an object inside a class
class A:
    x=5
p1=A()
print(p1.x)
#creating multiple objects
class A:
    x=25
p1=A()
p2=A()
p3=A()
print(p1.x)
print(p2.x)
print(p3.x)

#adding a new parameters
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

#__init__ method
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("John",25)
p2=person("emmu",32)
print(p1.name)
print(p2.age)

#default parameter
class customer:
    def __init__(self,name,age=20):
        self.name=name
        self.age=age
p1=customer("john")
p2=customer("ram",24)
print(p1.name , p1.age)
print(p2.name , p2.age)


#function with default parameters
def greet(name,message="Good Morning"):
    print(message,name)
greet("sandhya")


##function without default parameters
def greet(name,message):
    print(message,name)
greet("Pranathi","Good Morning")


#using init constructor with default parameters
class A:
    def __init__(self,name,message="Namaskaram"):
        self.message=message
        self.name=name
p1=A("ravi")
print(p1.message,p1.name)

#Q1
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return True
        else:
            return False
    def passorfail(self):
        if student.is_passed(self):
            print("pass")
        else:
            print("fail")

objA=student("ravi",65)
objB=student("raju",35)
objA.passorfail()
objB.passorfail()

#Q2
class employee:
    company_name=""
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name

objA=employee("hima")
objA.change_company("TCS")
print(objA.name)
print(objA.company_name)

#Q3-Inheritance

class A:
    x=10
class B(A):
    pass
obj=B()
print(obj.x)
obj=A()
print(obj.x)


#Q4
class Student:
    school_name = "ABC School"   # Class variable

    def __init__(self, name, marks):
        self.name = name          # Instance variable
        self.marks = marks        # Instance variable

# Creating objects
s1 = Student("Pranathi", 85)
s2 = Student("Kiran", 90)

print(s1.name, s1.school_name)
print(s2.name, s2.school_name)

# Changing class variable
Student.school_name = "XYZ School"
print(s1.school_name)
print(s2.school_name)

#changing instance variables
s1.name="charan"
print(s1.name,s1.school_name)

#Q5
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    #with str
    def __str__(self):
       return f"{self.name} scored {self.marks} marks"

s1 = Student("Pranathi", 95)

print(s1)

##without str method if you print the object it will print address
class student:
    def __init__(self,name):
        self.name=name

s1=student("pranathi")

print(s1.name)

#Q6
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

s = Student("Pranathi", 95)
print(s)     # Calls __repr__()

#Q7
class Student:
    def __init__(self, name, marks):     # Constructor
        self.name = name                 # Instance variable
        self.marks = marks

    def display(self):                   # Instance method
        print("Name:", self.name)        # Access instance variable using self
        print("Marks:", self.marks)      # Access instance variable using self
s1 = Student("Pranathi", 95)
s1.display()


#Q8-*args
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)
    print(args)
add_numbers(10, 20)
add_numbers(5, 10, 15, 20)

#Q9
class student:
    school_name="ABC School"      #class variable
    def __init__(self,name,marks):#constructor
        self.name=name          #instance variables
        self.marks=marks        #instance variables
    def display(self):          #instance method
        print("Name:",self.name)
        print("marks:",self.marks)
    @classmethod                #classmethod
    def get_school(cls):
        print("SchoolName:",cls.school_name)
    @staticmethod               #@staticmethod
    def Welcome():
        print("Welcome to school portal")
s1=student("pranathi",90)
s1.display()                    #calling instancemethod by object
student.get_school()            #calling classmethod by class
student.Welcome()               #calling staticmethod by class

#Q10
class Cvcorp:
    batch="python"
    def __init__(self,building_name,road_no):
        self.building_name=building_name
        self.road_no=road_no
    def display(self):
        if self.road_no==1 or self.road_no==2:
            return self.building_name
        else:
            return "notfound"
    @classmethod
    def shift(cls,road_no):
        if road_no==1:
            Cvcorp.batch="java"
        elif road_no==2:
            Cvcorp.batch="new python batch"
        else:
            Cvcorp.batch="practice"
s1=Cvcorp("ABC",1)
print(s1.display())
Cvcorp.shift(s1.road_no)
print(Cvcorp.batch)

s2=Cvcorp("XYZ",2)
print(s2.display())
Cvcorp.shift(s2.road_no)
print(Cvcorp.batch)

s3=Cvcorp("DEF",3)
print(s3.display())
Cvcorp.shift(s3.road_no)
print(Cvcorp.batch)



#Q11
class student:
    school_name="ABC school"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
       # self.school_name=schoolname
    def show(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("SchoolName:",self.school_name)
    @classmethod
    def change_school(cls,newname):
        cls.schoolname=newname
s1=student("pranathi",90)#,"XYZ school")
s2=student("charan",80)#,"XYZ school")
s1.show()
s2.show()
s1.school_name="DEF school"
s1.show()
s2.show()

#Q12
class Employee:
    company_name="Techcrop"
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Employee:",self.name)
        print("CompanyName",self.company_name)
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
s1=Employee("pranathi")
s2=Employee("himabindu")
s3=Employee("himaswi")
s1.display()
s2.display()
s3.display()
Employee.company_name="GB Tech"
s1.display()
s2.display()
s3.display()

#Q13
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>40:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>91:
            return "A"
        elif marks>81:
            return "B"
        else:
            return "C"
for _ in range(3):
    name=input("enter the name")
    marks=int(input("enter the marks"))
    s1=Student(name,marks)
    s1.result()
    print(s1.grade_category(s1.marks))


#Q14
class Student:
   passing_marks=40
   def __init__(self,name,marks):
       self.name=name
       self.marks=marks
   def result(self):
       if self.marks>=self.passing_marks:
           print("Pass")
           return
       print("Fail")
   @classmethod
   def update_passing_marks(cls,new_marks):
       cls.passing_marks=new_marks
   @staticmethod
   def grade_category(grade):
       if grade>=90:
           print("A")
       elif grade>=80:
           print("B")
       else:
           print("C")

for _ in range(3):
   name=input("Enter your name: ")
   marks=int(input("Enter your marks: "))
   student=Student(name,marks)
   student.result()
   student.grade_category(student.marks)

#Q15
class BankAccount:
     bank_name="HDFC"
     def __init__(self,holder,balance):
         self.holder=holder
         self.balance=balance
     def deposit(self,amount):
         self.balance=self.balance+amount
     @classmethod
     def change_bank_name(cls,new_name):
         cls.bank_name=new_name
     @staticmethod
     def validate_amount(amount):
         return amount>0
acc1=BankAccount("Pratyusha", 10000000)
print(acc1.balance)#10000000
print(BankAccount.validate_amount(acc1.balance))#True
acc1.deposit(10000000)
print(acc1.balance)#20000000
acc1.change_bank_name("Axis")
print(BankAccount.bank_name)#Axis
print(acc1.bank_name)#Axis
BankAccount.change_bank_name("SBI")
print(acc1.bank_name)#SBI
print(BankAccount.bank_name)#SBI











