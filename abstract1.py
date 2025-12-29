#6. Create a python application where we have one abstract class,
# which contains one parameterized constructor, one defined method, and two abstract methods,
# we also have one concrete class which contains one defined method and one parameterized constructor,
# then inherit both these classes into another concrete class to provide functionality for abstract methods
# and invoke all the properties under main method by providing dynamic inputs.
from abc import ABC,abstractmethod
class A(ABC):
    def __init__(self,a):
        self.a=a
    def m1(self):
        print(self.a)
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
class B:
    def __init__(self,a):
        self.a=a
    def m4(self):
        print(self.a)
class C(A,B):
    def m2(self):
        print("Hi")
    def m3(self):
        print("Hello")
obj=C(10)
obj.m1()
obj.m2()
obj.m3()
obj.m4()




#11. Using abc module:
# Create an abstract class Shape with area(), perimeter()
#• Implement Circle, Rectangle, Triangle
#Demonstrate:
# why base class should NOT contain calculation logic
# what happens if a subclass fails to implement one of the methods

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class circle(shape):
    def area(self):
        print("area")
    def perimeter(self):
        print("perimeter")
class rectangle(shape):
    def area(self):
        print("area1")
    def perimeter(self):
        print("perimeter1")
class triangle(shape):
    def area(self):
        print("area2")
    def perimeter(self):
        print("perimeter2")
class abc(shape):
    def area(self):
       pass
        #print("123")
    def perimeter(self):
        pass
p1=abc()
p1.area()
p1.perimeter
obj1=circle()
obj2=rectangle()
obj3=triangle()
obj1.area()
obj1.perimeter()
obj2.area()
obj2.perimeter()
obj3.area()
obj3.perimeter()
#a=abc()
#a.area()

#12. Design an abstract class PaymentGateway with:
# authenticate()
# pay(amount)
# refund(amount)
#Implement subclasses:
# UPIPayment
# CardPayment
# NetBankingPayment
#Show how abstraction helps your main program call payment methods without caring about
#the payment type.

from abc import ABC,abstractmethod
class paymentgate(ABC):
      @abstractmethod
      def authenticate(self):
          pass
      @abstractmethod
      def pay(self,amount):
          pass
      @abstractmethod
      def refund(self,amount):
          pass
class upipayment(paymentgate):
    def authenticate(self):
        print("authenticate upi..")
    def pay(self,amount):
        print(f'paid {amount} using upi')
    def refund(self,amount):
        print(f'refunded {amount} upi')
class cardpayments(paymentgate):
    def authenticate(self):
        print("authenticate card")
    def pay(self,amount):
        print(f'paid {amount} card')
    def refund(self,amount):
        print(f'refunded {amount} card')
class netbankingpayment(paymentgate):
    def authenticate(self):
        print("authenticate net banking")
    def pay(self,amount):
        print(f'paid {amount} net banking')
    def refund(self,amount):
        print(f'refunded {amount} netbanking')
def process_payment(payment,amount):
    payment.authenticate()
    payment.pay(1000)
    payment.refund(amount)
upi=upipayment()
card=cardpayments()
net=netbankingpayment()
process_payment(upi,2000)
print()
process_payment(upi,1000)
print()
process_payment(net,1500)

#13. Create:
# Abstract class VehicleControl with methods accelerate(), brake(), steer()
# Implement CarControl, BikeControl, TruckControl
#Demonstrate calling each through a single interface.

from abc import ABC,abstractmethod
class vehiclecontrol(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def steer(self):
        pass
class carcontrol(vehiclecontrol):
    def accelerate(self):
        print("car accelarate")
    def brake(self):
        print("car brake")
    def steer(self):
        print("car steer")
class bikecontrol(vehiclecontrol):
    def accelerate(self):
        print("bikecontrol accelarate")
    def brake(self):
        print("bikecontrol brake")
    def steer(self):
        print("bikecontrol steer")
class truckcontrol(vehiclecontrol):
    def accelerate(self):
        print("truckcontrol accelarate")
    def brake(self):
        print("truckcontrol brake")
    def steer(self):
        print("truckcontrol steer")
#def operate(vehicle,vehiclecontrol):
def operate(vehicle):
    vehicle.accelerate()
    vehicle.brake()
    vehicle.steer()
#car=carcontrol()
bike=bikecontrol()
Truck=truckcontrol()
operate(carcontrol())
operate(bike)
operate(Truck)

#14. Create an abstract class DatabaseDriver with:
# connect()
# execute(query)
# close()
# Implement concrete drivers:
# MySQLDrive
# PostgresDriver
# SQLiteDriver
#Show how abstraction helps switch databases without rewriting main code.

from abc import ABC,abstractmethod
class databasedriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self,query):
        pass
    @abstractmethod
    def close(self):
        pass
class mysqldriver(databasedriver):
    def connect(self):
        print("mysqldriver connect")
    def execute(self,query):
        print("mysqldriver execute")
    def close(self):
        print("mysqldriver close")
class postgresdriver(databasedriver):
    def connect(self):
        print("postgresdriver connect")
    def execute(self,query):
        print("postgresdriver execute")
    def close(self):
        print("postgresdriver close")
def operate(subject):
    subject.connect()
    subject.execute("SELECT* FROM users")
    subject.close()
operate(mysqldriver())
print()
operate(postgresdriver())

#15. Design a class ReportGenerator (abstract) with:
# load_data()
#• process()
#• export()
#Implement:
#• PDFReport
#• ExcelReport
#Demonstrate how abstraction enforces a multi-step structure.

from abc import ABC,abstractmethod
class reportgenerator(ABC):
    @abstractmethod
    def load_data(self):
        pass
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def export(self):
        pass
    def generate(self):
        self.load_data()
        self.process()
        self.export()
class pdfreport(reportgenerator):
    def export(self):
        print("pdf:exporting data")
    def load_data(self):
        print("pdf:loading data")
    def process(self):
        print("pdf:processing data")
class excelreporter(reportgenerator):
    def load_data(self):
        print("excel:loading data")
    def process(self):
        print("excel:processing data")
    def export(self):
        print("excel:exporting data")
obj1=pdfreport()
obj2=excelreporter()
obj1.generate()
obj2.generate()

#16. Create an abstract class RobotCommand with:
#• execute()
#• undo()
#Implement:
#• PickCommand
#• PlaceCommand
#• MoveCommand
#Demonstrate how abstraction cleanly represents commands without revealing details.

from abc import ABC,abstractmethod
class robotcommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class pickcommand(robotcommand):
    def execute(self):
        print("robot:picking up item")
    def undo(self):
        print("undo:picking item back")
class placecommand(robotcommand):
    def execute(self):
        print("execute:placing up item")
    def undo(self):
        print("undo:placing item back")
class movecommand(robotcommand):
        def _init_(self, direction):
            self.direction = direction

        def execute(self):
            print(f"Robot: Moving {self.direction}")

        def undo(self):
            print(f"Undo: Moving opposite of {self.direction}")
def run_command(command:robotcommand):
    command.execute()
    command.undo()
    print()

run_command(pickcommand())
run_command(placecommand())
run_command(movecommand("right"))




