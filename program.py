person = {}

while True :
    name = input("Enter name :");
    age = input("Enter age :");
    person[name] = age
    ask=input("Another ? y/n :");

    if ask== "y" :
        continue
    else :
        break

for (key,value) in person.items():
    print(f'{key} is {value} years old');
    


