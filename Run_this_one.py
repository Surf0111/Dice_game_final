import Data_handling
import pandas as pd
import Prompts
import pyautogui
import random
import time
from cryptography.fernet import Fernet
global p1_total
global p2_total


# allows two players to enter their details, which are then autheticated
# allows each player to roll 2 6 sided dice
# calculated and outputs the points for each round and total score
# play 5 rounds
# if both have the same score after 5 rounds, allow each to roll 1 more dice until someone wins
# outputs who has won
# stores the winners score and name in csv dile
# displays the score and player name of the top 5 winning scores


def doubles(num, player, x):
    pyautogui.confirm(f'{player} rolled a double! You got {num} bonus points!', title=f'Round {x}')

# this outputs the value of the roll to the screen
def roll_out(num, player, x):
    pyautogui.confirm(f'{player} rolled {num}!', title=f'Round {x}')


def round_results(p1, r1, p2, r2, x):
    pyautogui.alert(f'{p1}: {r1} points\n{p2}: {r2}', title=f'Round {x}')

# this shows the players a running total of the 
def totals(p1, t1, p2, t2):
    pyautogui.alert(f'{p1}: {t1} points\n{p2}: {t2}', title='Total')


def pause():
    time.sleep(2)


def roll(p1, p2, x):
    global p2_round_total, p1_round_total
    r1_p1 = random.randint(1,6)
    roll_out(r1_p1,p1, x)
    r2_p1 = random.randint(1,6)
    roll_out(r2_p1, p1, x)
    p1_round = r1_p1 + r2_p1

    # for player one:
    # if total is even +10 points
    # if total is odd -5 points
    # if doubles + single dice roll

    if r1_p1 == r2_p1:
        double_p1 = random.randint(1,6)
        doubles(double_p1, p1, x)
        p1_round += double_p1
        p1_round_total = p1_round

    elif (p1_round % 2) == 0:
        p1_round_total = 10 + p1_round
        p1_add(p1_round_total)

    else:
        temp = p1_round - 5
        if temp <= 0:
            p1_add(0)
            p1_round_total = p1_round
        else:
            p1_round_total = p1_round - 5
            p1_add(p1_round_total)

    pause()
    # for player two:
    # if total is even +10 points
    # if total is odd -5 points
    # if doubles + single dice roll

    r1_p2 = random.randint(1, 6)
    roll_out(r1_p2, p2, x)
    r2_p2 = random.randint(1, 6)
    roll_out(r2_p2, p2, x)
    p2_round = r1_p2 + r2_p2

    if r1_p2 == r2_p2:
        double_p2 = random.randint(1, 6)
        doubles(double_p2, p1, x)
        p2_round += double_p2
        p2_round_total = p2_round

    elif (p2_round % 2) == 0:
        p2_round_total = 10 + p2_round
        p2_add(p2_round_total)

    else:
        temp = p2_round - 5
        if temp <= 0:
            p2_add(0)
            p2_round_total = p2_round
        else:
            p2_round_total = p2_round - 5
            p2_add(p2_round_total)

    round_results(p1, p1_round_total, p2, p2_round_total, x)

    t1 = sum(p1_total)
    t2 = sum(p2_total)
    totals(p1, t1, p2, t2)

# adds the score to the list of results
def p1_add(score):
    global p1_total
    p1_total.append(score)


def p2_add(score):
    global p2_total
    p2_total.append(score)


def tiebreak(p1, p2, x):

    r1_p1 = random.randint(1, 6)
    roll_out(r1_p1, p1, x)
    global p1_total
    p1_total.append(r1_p1)

    r1_p2 = random.randint(1, 6)
    roll_out(r1_p2, p2, x)
    global p2_total
    p2_total.append(r1_p2)

    if sum(p1_total) == sum(p2_total):
        pyautogui.alert('The scores are still even, the tiebreak continues!')
        tiebreak(p1, p2, x)

    elif sum(p1_total) > sum(p2_total):
        Data_handling.write_score(player_1, p1_total)
        p1_total_sum = sum(p1_total)
        Prompts.winner(player_1, p1_total_sum)
    else:
        Data_handling.write_score(player_2, p2_total)
        p2_total_sum = sum(p1_total)
        Prompts.winner(player_2, p2_total_sum)




def game():
    global x
    for x in range(1,6):
        roll(player_1, player_2, x)
        pause()

    if sum(p1_total) != sum(p2_total):
        if sum(p1_total) > sum(p2_total):
            Data_handling.write_score(player_1, p1_total)
            Prompts.winner(player_1, p1_total)
        else:
            Data_handling.write_score(player_2, p2_total)
            Prompts.winner(player_2, p2_total)
    else:
        while sum(p1_total) == sum(p2_total):
            tiebreak(player_1, player_2, 'Tiebreak')


# main
print('''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗    
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║       ██║   ███████║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║       ██║   ██╔══██║██╔══╝      
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝    
                                                                                                                     
                        ██████╗ ██╗ ██████╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗                          
    ▄ ██╗▄    ▄ ██╗▄    ██╔══██╗██║██╔════╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ▄ ██╗▄    ▄ ██╗▄      
     ████╗     ████╗    ██║  ██║██║██║     █████╗      ██║  ███╗███████║██╔████╔██║█████╗       ████╗     ████╗      
    ▀╚██╔▀    ▀╚██╔▀    ██║  ██║██║██║     ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ▀╚██╔▀    ▀╚██╔▀      
      ╚═╝       ╚═╝     ██████╔╝██║╚██████╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗      ╚═╝       ╚═╝       
                        ╚═════╝ ╚═╝ ╚═════╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                          
                                                                                                                     
''')

player_1 = Prompts.prompt_p1()
print(f'Welcome, {player_1}!')
player_2 = Prompts.prompt_p2()
if player_2 == player_1:
    Prompts.same_account()
print(f'Welcome, {player_2}!')

p1_total = []
p2_total = []

game()
Prompts.end_prompt()



