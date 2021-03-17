#coinflip

import os

def coinflipFunc():


        flip = input("Heads or Tails? ").lower()
        
        if flip in ["heads", "tails"]:
                
                bet = int(input("How much? "))
                
                if isinstance(float(bet), (int, float)):               
                        import random
                        x = random.randint(1, 2)

                        isEven = (x % 2 == 0)

                        if isEven:
                                print("Heads,")
                                if flip == "heads":
                                        print("you won $" + str(bet) + "!")
                                if flip == "tails":
                                        print("you lost $" + str(bet) + "!")
                        if isEven == False:
                                print("Tails,")
                                if flip == "heads":
                                        print("you lost $" + str(bet) + "!")
                                if flip == "tails":
                                        print("you won $" + str(bet) + "!") 

        else:
                print("That wasn't a choice, silly!") 
        
coinflipFunc()
os.system("pause")