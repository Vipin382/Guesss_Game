import random
print("In This game you have to guess the number Between 1 to 20.You have 6 Lives Lest")
while True:
    x = input("You Wanna Play this Game.Type Y for yes and N to quit: ")
    a = random.randint(1,20)
    t = 7
    i = 20
    if x=="Y":
        while True:
            t = t-1
            if t==0:
                print("You are out of lives.\nYOU LOOSE!!!")
                print("Number to be Guessed is ",a)
                break
            else:
                n = int(input("Guess the number: "))
                print("Total Lives Left are ",t)
                if n==a:
                    print("You Won!,your Guess is correct,")
                    i = i+1
                    print("Your Score is: ",i)
                    break
                elif n<a:
                    print("Your Guess is Low ,Try Higher Number")
                    i = i-1
                    print("Your Score is: ",i)
                    continue
                elif n>a:
                    print("Your Guess is High,Try Lower Number")
                    i = i-1
                    print("Your Score is: ",i)
                    continue
    elif x=="N":
        print("Thank You!.For Playing the game .Hope! you like it.")
        break
    else:
        print("You write the Typed the wrong Number or letter,Try again")
        continue
