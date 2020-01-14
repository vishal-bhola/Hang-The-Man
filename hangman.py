import random


def hangman():
    word=random.choice(["pugger","tiger","lion","cheetah","thor","ironman","superman","blackwidow","hawkeye","mother","country","pegion",
                        "carrot","cricket","hockey","technical","human","bad","amazing","hulk","god","picture","air","laptop",
                        "pokemon","avengers","savewater","strangerthings","lostinspace","selena","justice","doctor","hospital","youtube","night",
                        "annabelle","rockstar","mindflayer","dragons"])

    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""

    while len(word)>0:
        main = "" 
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" +" "   
        if main == word:
            print("'%s'"%main)
            print("Congratulations!!!You Win.")
            print("You saved the kind man")
            break
        
        print("Guess the word(all in small): ",main) 
        guess = input()

        if guess in validLetters:
            if guess in main:
                print("You have already guessed that character!")
            else:
                guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns==9:
                print("9 turns left")
                print(" --------- ")
            if turns == 8:
                print("8 turns left")
                print(" --------- ")
                print("     O     ")
            if turns == 7:
                print("7 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
            if turns == 6:
                print("6 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
                print("    /      ")
            if turns == 5:
                print("5 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")        
                print("    / \    ")        
            if turns == 4:
                print("4 turns left")
                print(" --------- ")
                print("   \ O     ")
                print("     |     ")        
                print("    / \    ")   
            if turns == 3:
                print("3 turns left")
                print(" --------- ")
                print("   \ O /   ")
                print("     |     ")        
                print("    / \    ")
            if turns == 2:
                print("2 turns left")
                print(" --------- ")
                print("   \ O /|  ")
                print("     |     ")        
                print("    / \    ")   
            if turns == 1:
                print("1 turn left")
                print("Last breathe counting, Take care!")
                print(" --------- ")
                print("   \ O_|/  ")
                print("     |     ")        
                print("    / \    ")                   
            if turns == 0:
                print("Word is '%s'"%word)
                print("You loose!!")
                print("You let a kind man die")
                print(" --------- ")
                print("     O_|   ")
                print("    /|\    ")        
                print("    / \    ")
                break    


name = input("Enter your name:- ")   
while len(name)==0:
    name= input("Firstly, Enter your name :- ")
print("Welcome",name)
print("-----------------")
print("Try to guess the word in less than 10 try")

hangman()