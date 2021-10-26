class Car:
    def __init__(self,name,license,color):
        self.name = name
        self.license =license
        self.color = color
    def drive(self):
        print(f'{self.name} is driving');
    def isLicensed(self):
        if self.license==True:
            print("It has license");
        else :
            print("Without!");

lambo = Car("Lamborghini", True,"Red");
lambo.drive();
lambo.isLicensed();

Marcedes = Car("Marcedes",False,"Black");
Marcedes.drive();
Marcedes.isLicensed();
