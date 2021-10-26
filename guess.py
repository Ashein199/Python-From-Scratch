num = 3 ;
guess = int(input("Guess number :"));

while guess != num :
    if guess < num :
        print("too low");
    else :
        print("too high");
    guess = int(input("Guess number :"));

print("Wow.. Correct!");