import random
def generate ():
    selection = 3
    mylist = ["Rock","Paper","Scissors"]
    selection = random.randint(0,2)
    return mylist[selection]

def compare (p1,p2):
    if p1 == p2:
        return "Draw!!!"
    if p1 == "Rock":
        if p2 == "Paper":
            return "PLayer 2 Won!!!"
        return "PLayer 1 Won!!!"
    if p1 == "Paper":
        if p2 == "Rock":
            return "PLayer 1 Won!!!"
        return "PLayer 2 Won!!!"
    if p1 == "Scissors":
        if p2 == "Rock":
            return "PLayer 2 Won!!!"
        return "PLayer 1 Won!!!"

while True:
    p1 = raw_input("You're Player 1, Enter Rock,Paper, or Scissors or -1 to Exit: ")
    if p1 == "-1":
        print "Game Ended."
        break
    p2 = generate()
    print "Player 1 : " + p1
    print "Player 2 : " + p2
    print compare(p1,p2)
    