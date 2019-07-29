from random import randint
p = 0
c = 0
player = input('Your call: (r for Rock, p for Paper and s for Scissor): ')
comp = randint(1,3)
if comp == 1:
    computer = 'r'
elif comp == 2:
    computer = 'p'
elif comp == 3:
    computer = 's'
else:
    print("invalid input!!!")
print(player,' vs ', computer)
def result(player, computer):
    if player == computer:
        print ("DRAW!!")
    else:
        if player == 'r' and computer == 'p':
            print("Computer Wins!")
        if player == 'p' and computer == 's':
            print("Computer Wins!")
        if player == 's' and computer == 'r':
            print("Computer Wins!")
        if player == 'r' and computer == 's':
            print("You Win!")
        if player == 'p' and computer == 'r':
            print("You Win!")
        if player == 's' and computer == 'p':
            print("You Win!")

result(player, computer)
