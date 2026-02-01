from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDb
from validation.email_validator import email_vali
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password
from cli.manager_menu import managerMainMenu


# this is obj for the employee repo
emp_db = EmployeeDb()
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignUp():
    print('employee signup')
    name = input('Enter ur name:')
    email = input('Enter your email:')
    verify_email = emp_db.searchEmp(email)
    if verify_email is None:
        if email_vali(email=email) is not None:
            password = getpass('Enter your password:')
            confirm_pw = getpass('Enter your password:')
            if password == confirm_pw:
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
            else:
                print("pasword and confirm password both are same so.. Enter again")
                employeeSignUp()

        else :
            print('''enter valid email id!!!!!!!!!!!!!!!!!!''')
            employeeSignUp()
    else:
        print(f'account with this Email id {email} is already exist . login')
        empolyeeLogin()

def empolyeeLogin():
    print('Employee Login')
    email = input("Enter your email id:")
    password = getpass('Enter your password:')
    data = emp_auth.empLogin(email)
    hashed_pw = data[3]
    is_manager = data[5]
    if check_password(password,hashed_pw):
        if is_manager == 1:
            print("Manager login successfully")
            managerMainMenu(data[0])
        else:
            print("Employee login successfully")
    else:
        print("login failed")