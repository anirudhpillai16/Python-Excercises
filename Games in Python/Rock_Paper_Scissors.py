# Rock Paper Scissor

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

player1= raw_input("Enter your name Player 1: ")
player2= raw_input("Enter your name Player 2: ")
print " Please choose one "
print " Rock: 1"
print " Paper: 2"
print " Scissor: 3"
c1 = input("Enter your choice Player1 :")
c2 = input("Enter your choice Player2 :")
if (c1 == c2):
    print "It's a tie! Try again"
elif c1 ==1 and c2== 2:
    print player2 + " wins as paper beats rock"
elif c1==1 and c2==3:
    print player1 + " wins as rock beats scissors"
elif c1==2 and c2==3:
    print player2 + " wins as scissor beats paper"
elif c1==2 and c2==1:
    print player1 + " wins as paper beats rock"
elif c1==3 and c2==1:
    print player2 + " wins as rock beats scissors"
elif c1==3 and c2 == 2:
    print player1 + " wins as scissor beats paper"
else:
    print "Something Wrong! Perhaps wrong choice"

    
    
