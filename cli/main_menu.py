from cli.employee_menu import employeeSignUp
def menu():
    while True:
        print('''welcome
press 1 for admin login
press 2 for employee singup
press 3 for employee login''')
        choice = int(input('enter your option:'))
        if choice == 1:
            pass
        elif choice == 2:
            employeeSignUp()
        elif choice == 3 :
            pass
        
