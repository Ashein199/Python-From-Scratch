print("How many miles do you want to convert?");
miles = input();
kms = float(miles) * 1.609344;
kms = round(kms,4);

print(f'Your kilometers is {kms} kms');