import Data_handling
from cryptography.fernet import Fernet
import Prompts


def get_key():
    file = open('key.key', 'rb')
    f = file.read()
    file.close()
    key = Fernet(f)
    return key


def validate_login(username, password):
    try:
        key = get_key()
        stored_password = Data_handling.fetch_password(username)
        decrypted_password = key.decrypt(stored_password).decode()
        if password == decrypted_password:
            return
        else:
            Prompts.wrong_password()
    except FileNotFoundError:
        Prompts.no_account()


def create_login(username, password):
    key = get_key()
    enc_password = key.encrypt(password.encode())
    Data_handling.write_account(username, enc_password)
