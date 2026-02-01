from passlib.hash import pbkdf2_sha256
from passlib.utils.binary import ab64_decode

# def password_hasher(password):
#     return pbkdf2_sha256.hash(password)

# def check_password(password,hash):
#     return pbkdf2_sha256.verify(password,hash)

def password_hasher(password):
    return pbkdf2_sha256.hash(password)

def check_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)


# my_password = password_hasher('Shiva@123')
# print(check_password('Shiva@123'),my_password)
