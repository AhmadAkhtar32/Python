#Practice Question 2
import random

def game():
    print("You Are Playing A Game! ")
    score = random.randint(0,99)
    #fetch the high score
    with open("Chapter9/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your Score is : {score}")
    if(score>hiscore):
        #Write this score to the file
        with open("Chapter9/hiscore.txt", "w") as f:
         f.write(str(score))
    return score

game()