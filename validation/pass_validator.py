from password_validator import PasswordValidator

schema = PasswordValidator()
schema.min(5)
schema.max(50)
schema.has().uppercase()
schema.has().symbols()
schema.has().digits()


# print(schema.validate('vail'))

def password_vali(password):
    return schema.validate(password)





