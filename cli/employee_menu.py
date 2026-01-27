from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDb
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password


# this is obj for the employee repo
emp_db = EmployeeDb()
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignUp():
    print('employee signup')
    name = input('Enter ur name:')
    email = input('Enter your email:')
    if email_vali(email=email) is not None:
        password = getpass('Enter your password:')
        if password_vali(password):
            password = password_hasher(password)
            emp_auth.createEmployee(name,email,password)
        else:
            print('''password is not valid
                  password should length of 5
                  password should contain atleast uppercase character ex: A X H
                  password should contain atleast speical character EX: @ _ #
                  password should contain atleast number character EX: 1233''')
            employeeSignUp()
    else :
        print('''enter valid email id!!!!!!!!!!!!!!!!!!''')
        employeeSignUp()

def empolyeeLogin():
    print('Employee Login')
    email = input("Enter your email id:")
    password = getpass('Enter your password:')
    hashed_pw = emp_auth.empLogin(email)
    if check_password(password,hashed_pw):
        print("login successfully")
    else:
        print("login failed")
