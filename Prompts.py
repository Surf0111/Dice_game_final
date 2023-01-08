import pyautogui
import Data_handling
import Encryption



def prompt_p1():
    option = pyautogui.confirm('Welcome Player 1', buttons =['Leaderboard', 'Login', 'New account'], title='Dice game')
    if option == 'Login':
        username = pyautogui.prompt('Username')
        password = pyautogui.password('Password')
        Encryption.validate_login(username, password)
        x = username
        return x

    elif option == 'New account':
        username = pyautogui.prompt('Username', title='Player 1')
        password = pyautogui.password('Password', title='Player 1')
        Encryption.create_login(username, password)
        x = username
        return x

    elif option == 'Leaderboard':
        leader_board = Data_handling.fetch_score()
        print(leader_board)
        pyautogui.alert(leader_board, title='Leaderboard')
        raise SystemExit

    else:
        None

def prompt_p2():
    option = pyautogui.confirm('Welcome Player 2', buttons=['Login', 'New account'], title='Dice game')
    if option == 'Login':
        username = pyautogui.prompt('Username', title='Player 2')
        password = pyautogui.password('Password', title='Player 2')
        Encryption.validate_login(username, password)
        x = username
        return x

    elif option == 'New account':
        username = pyautogui.prompt('Username')
        password = pyautogui.password('Password')
        Encryption.create_login(username, password)
        x = username
        return x


def end_prompt():
    option = pyautogui.confirm('Enter option Gfg', buttons=['Leaderboard', 'New game', 'Exit'], title='Dice game')
    if option == 'Leaderboard':
        x = Data_handling.fetch_score()
        print(x)
        pyautogui.alert(x)


def account_error():
    pyautogui.alert('Error. Account already exists. Try again')
    raise SystemExit


def same_account():
    pyautogui.alert('Error. Only two different users can play.')
    raise SystemExit


def no_account():
    pyautogui.alert("Error. This account doesn't exist.")
    raise SystemExit


def wrong_password():
    pyautogui.alert("Error. Wrong password.")
    raise SystemExit


def winner(player, total):
    score = total
    # this was done to remove the [] around the number without causing an error
    points = score[0]
    pyautogui.alert(f'{player} won with a total of {points} points!', title=f'Congratulations {player}!')
    raise SystemExit