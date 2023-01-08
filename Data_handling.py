import pandas as pd
import os.path
import pyautogui
import Prompts
import csv


def fetch_password(username):
    file = open(f'Logins/{username}.txt', 'rb')
    passwrd = file.read()
    return passwrd


def write_account(username, password):
    if not os.path.exists(f'Logins/{username}.txt'):
        with open(f'Logins/{username}.txt', 'wb') as file:
            file.write(password)
    else:
        Prompts.account_error()
        raise SystemExit


def write_score(username,score):
    with open('Hi_scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username] + score + [''])


# stop displaying the brackets and index


def fetch_score():
    df = pd.read_csv('Hi_scores.csv')
    df_sorted = df.sort_values(by=['Score'], ascending=False).to_string(index=False)
    return df_sorted


