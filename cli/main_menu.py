from cli.employee_menu import employeeSignUp,empolyeeLogin
from cli.admin_menu import adminLogin
from repositories.employee_repo import EmployeeDb

emp_db = EmployeeDb()

def menu():
    while True:
        print('''welcome
press 1 for admin login
press 2 for employee singup
press 3 for employee login''')
        choice = int(input('enter your option:'))
        if choice == 1:
            adminLogin()
        elif choice == 2:
            employeeSignUp()
        elif choice == 3 :
            empolyeeLogin()
        else:
            print("enter vaild data")
            
        
