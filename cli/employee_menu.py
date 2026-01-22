from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDb

# this is obj for the employee repo
emp_db = EmployeeDb()
emp_auth = EmployeeAuthentication(emp_db)

def employeeSignUp():
    print('employee signup')
    name = input('Enter ur name:')
    email = input('Enter your email')
    password = input('enter your password')
    emp_auth.createEmployee(name,email,password)

def empolyeeLogin():
    print('Employee Login')
    