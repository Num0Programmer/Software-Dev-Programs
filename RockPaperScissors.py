import random as rand
import os


#### Imports above


global again
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0


def clear():
  os.system('clear')




# Introduce the game, and initialize game variabels
def Start():
  global players

  print("This is a text based game of Rock, Paper, Scissors. If you are playing with another person, please try to refrain from looking the the screen while your opponent is typing their choice into the prompt.\n")

  num_of_players = str(input('Will you be playing with another person (y/n)?\n'))

  if num_of_players.lower() == 'y':
    players = 2
  else:
    players = 1

  clear()




def main():
  #global again
  again = True
  Start()
  # if there is one player, use computer
  if players == 1:
    while again == True:
      OnePlayer()
      again = End()
    
    print('Good game!')
  # if there are two players, use two players
  if players == 2:
    while again == True:
      TwoPlayers()
      again = End()
    
    print('Good game!')




def End():
  again = str(input('\nWould you like to play again (y/n)?\n'))

  if again.lower() == 'y':
    clear()
    return True
  else:
    clear()
    return False
  



def Change_To_Num(play):
  plays = {'rock': 0, 'paper': 1, 'scissors': 2}
  return plays[play]




def Computer_Choice():
  return rand.choice(['rock', 'paper', 'scissors'])




def OnePlayer():
  #while again == True:
  # Gets player's choice
  player1_play = str(input("Player one, what will you choose ('rock', 'paper', or 'scissors')?\n"))
  player_play = Change_To_Num(player1_play.lower()) # Sets player's

  clear() # Clears the screen

  # Gets computer's choice
  computer_play = Change_To_Num(Computer_Choice()) # Sets computer's choice
    
  Compare(player_play, computer_play)




def TwoPlayers():
  #while again == True:
  # Gets Player one's choice
  player1_play = str(input("Player one, what will you choose ('rock', 'paper', or 'scissors')?\n"))
  player1_play = Change_To_Num(player1_play.lower()) # Sets player's

  clear() # Clears the screen

  player2_play = str(input("Player two, what will you choose ('rock', 'paper', or 'scissors')?\n"))
  # Gets Player two's choice
  player2_play = Change_To_Num(player2_play.lower()) # Sets player's choice

  clear()

  Compare(player1_play, player2_play)




def Compare(player1_choice, player2_choice):
  global PLAYER1_SCORE
  global PLAYER2_SCORE

  if players == 2:
    if (player1_choice - player2_choice) % 3 == 1:
      # Player one wins
      print('Congratualtions Player One, you win this round!\n')
      # Increase score
      PLAYER1_SCORE = PLAYER1_SCORE + 1
    elif player1_choice == player2_choice:
      # Tie
      print("It's a tie, no dice.\n")
    else:
      # Player two wins
      print('Congratulations Player Two, you win this round!\n')
      # Increase score
      PLAYER2_SCORE = PLAYER2_SCORE + 1

  else:
    if (player1_choice - player2_choice) % 3 == 1:
      # Player one wins
      print('Congratualtions, you win this round!\n')
      # Increase score
      PLAYER1_SCORE = PLAYER1_SCORE + 1
    elif player1_choice == player2_choice:
      # Tie
      print("It's a tie, no dice.\n")
    else:
      # Player two wins
      print('Congratulations to the Computer, it wins this round!\n')
      # Increase score
      PLAYER2_SCORE = PLAYER2_SCORE + 1

  Display_Round_Results(PLAYER1_SCORE, PLAYER2_SCORE)




def Display_Round_Results(PLAYER1_SCORE, PLAYER2_SCORE):
  if players == 2:
    print('{:^17}\n'.format('Score'),
        '{:} : {:}\n'.format('Player One', PLAYER1_SCORE), 
        '{:} : {:}'.format('Player Two', PLAYER2_SCORE))
  else:
    print('{:^17}\n'.format('Score'),
        '{:} : {:}\n'.format('You', PLAYER1_SCORE), 
        '{:} : {:}'.format('Computer', PLAYER2_SCORE))




main()
