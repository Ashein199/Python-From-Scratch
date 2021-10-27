class RestaurantTable:

    menus={
        "pizza" : 5000,
        "cola" : 500,
        "hamburger" : 2000,
        "potato fries" : 1500,
        "juice" : "1000"
    }

    def __init__(self):
        self.total = 0;
        self.orders =[];

    def addOrder(self,order):
        self.orders.append(order);
        self.total +=self.menus[order];

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}') ;
        print(f'Total price is {self.total}')

def startOrder():
    table = RestaurantTable();
    print(table.menus);

    while True:
        order = input("order :");
        table.addOrder(order);

        another =input("order more? y/n :")
        if another == "y":
            continue;
        elif another == "n":
            table.printBill();
            break;
        else :
            table.printBill();
            break;
            
startOrder();


