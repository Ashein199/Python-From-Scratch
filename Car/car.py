class Car:
    steeringWheel = 1  #class level object
    def __init__(self,name,license,color):#instance object
        self.name = name
        self.license =license
        self.color = color
    def drive(self):
        print(f'{self.name} is driving');
    def isLicensed(self): #instance level method
        if self.license==True:
            print("It has license");
        else :
            print("Without!");
    @classmethod
    def common(cls): #class level
        print(f'All cars have only {cls.steeringWheel} steering wheel');

# lambo = Car("Lamborghini", True,"Red");
# lambo.drive();
# lambo.isLicensed();

# Marcedes = Car("Marcedes",False,"Black");
# Marcedes.drive();
# Marcedes.isLicensed();

print(Car.steeringWheel);
Mark = Car("Mark",True,"White");
Mark.common();
