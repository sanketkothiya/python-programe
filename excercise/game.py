import random
winning_number=random.randint(1,100)
guess=1
number=int(input("enter the number between 1 to 100"))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"you win the game and guess  the value for {guess} time")
        game_over=True
    else:
        if number<winning_number:
            print("to low")
        else:
            print("to high")
        guess+=1
        number=int(input("enter again"))