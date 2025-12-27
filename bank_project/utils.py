import hashlib
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('utils module initialized')

def hash_password(password):
    '''
    description : it hashes the password
    Arguments:
        password : string
    Returns:
        hashed_password : string
    Raises:
        Exception : if the password is not hashed

    '''
    try:
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    except Exception as e:
        logger.error(f'Error hashing password: {e}')
        return None


def check_password(hashed_password,plain_password):
    if hashed_password==hash_password(plain_password):
        return True
    else:
        return False



'''
import bcrypt

def advanced_hash_password(password):
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(hashed_password, plain_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))





from argon2 import PasswordHasher

ph = PasswordHasher()

def advanced_hash_password(password):
    return ph.hash(password)

def check_password(hashed_password, plain_password):
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except:
        return False




import hashlib
import secrets

def advanced_hash_password(password):
    salt = secrets.token_hex(16)  # Generate random salt
    iterations = 100000  # Number of iterations
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    return f"{salt}:{iterations}:{hashed.hex()}"

def check_password(hashed_password, plain_password):
    salt, iterations, stored_hash = hashed_password.split(':')
    iterations = int(iterations)
    new_hash = hashlib.pbkdf2_hmac('sha256', plain_password.encode(), salt.encode(), iterations)
    return new_hash.hex() == stored_hash


import hashlib
import secrets

def advanced_hash_password(password):
    salt = secrets.token_hex(16)
    hashed = hashlib.scrypt(password.encode(), salt=salt.encode(), n=16384, r=8, p=1)
    return f"{salt}:{hashed.hex()}"

def check_password(hashed_password, plain_password):
    salt, stored_hash = hashed_password.split(':')
    new_hash = hashlib.scrypt(plain_password.encode(), salt=salt.encode(), n=16384, r=8, p=1)
    return new_hash.hex() == stored_hash

'''






