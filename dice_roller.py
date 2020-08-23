import random 

def main():
#Player1
 dice_player1 = input('Tell me who you are:')
 print(f'For {dice_player1}')
 dice_rolls1 = int(input('How many dice would you like to roll? '))
 dice_size1 = int(input('How many sides are the dice? '))
 dice_sum1 = 0
 for i in range(0,dice_rolls1):
   roll1 = random.randint(1,dice_size1)
   dice_sum1 = dice_sum1 + roll1
   if roll1 == 1:
     print(f'You rolled a {roll1}! Critical Fail')
   elif roll1 == dice_size1:
     print(f'You rolled a {roll1}! Critical Success!')
   else:
     print(f'You rolled a {roll1}')
 print(f'Congratulations {dice_player1}, you have rolled a total of {dice_sum1}')
 
 #Player2
 dice_player2 = input('Tell me who you are:')
 print(f'For {dice_player2}')
 dice_rolls2 = int(input('How many dice would you like to roll? '))
 dice_size2 = int(input('How many sides are the dice? '))
 dice_sum2 = 0
 for i in range(0,dice_rolls2):
   roll2 = random.randint(1,dice_size2)
   dice_sum2 = dice_sum2 + roll2
   if roll2 == 1:
     print(f'You rolled a {roll2}! Critical Fail')
   elif roll2 == dice_size2:
     print(f'You rolled a {roll2}! Critical Success!')
   else:
     print(f'You rolled a {roll2}')
 print(f'Congratulations {dice_player2}, you have rolled a total of {dice_sum2}')
 if dice_sum2> dice_sum1:
   print(f'Congratulations {dice_player2}, you have rolled more than {dice_player1}')
 elif dice_sum2< dice_sum1:
   print(f'Congratulations {dice_player1}, you have rolled more than {dice_player2}')
 else:
   print(f'{dice_player1}, you have rolled the same as {dice_player2}')

if __name__== "__main__":
  main()