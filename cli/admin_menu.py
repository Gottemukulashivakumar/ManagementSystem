from getpass4 import getpass
from dotenv import load_dotenv
import os
from services.auth import AdminAuthentication
from repositories.employee_repo import EmployeeDb
from repositories.manager_repo import managerDb
from repositories.request_repo import RequestDb
from services import admin_services


emp_db = EmployeeDb()
mgr_db = managerDb()
req_db = RequestDb()
admin_auth = AdminAuthentication(emp_db,mgr_db,req_db)

load_dotenv()


def adminWelcome():
    print('welcome back Admin')

def adminLogin():
    password = getpass("Enter your password")
    if password == os.getenv('ADMIN_PW'):
        adminMainMenu()
    else:
        print("password is incorrect tey to login again")
        adminWelcome()
        adminLogin()

def allEmplo():
    emp_datas = admin_auth.db.getAllEmp()
    for emp_data in emp_datas:
            print(f'''
____________________________________________
employee id : {emp_data[0]}                |
employee name : {emp_data[1]}              |  
employee email : {emp_data[2]}             |
employee manager id : {emp_data[3]}        | 
___________________________________________|''')
    adminMainMenu()

def managerPromotion():
    id = int(input("enter the employee id to promote to manager:"))
    data = admin_auth.db.getEmp(id)
    # print(data, len(data))
    if data[5] == 0:
        if  data is not None:
            admin_auth.db.modifyEmptomgr(id)
            adminMainMenu()
        else:
            print("employee id {id} is not present")
            managerPromotion()
    else:
        print(f'employee with id {id} is already a manager try with some other empolyee id')
        managerPromotion()


def adminMainMenu():
    print('welcome back Admin')
    Choice = int(input('''
-------------------------------------------------------
|press 1 for all employee data                        |
|press 2 for all manager data                         |
|press 3 for for promote employee to manager           | 
|press 4 for assign project to manager                |
|press 5 for see the manager request for employee     | 
|press 6 for assgin employee to manager               |
|press 7 for check the update of the project          |
|press 8 for logout                                   |
-------------------------------------------------------
enter your choice:'''))
    
    if Choice == 1 :
        allEmplo()

    elif Choice == 2 :
        mgr_datas = admin_auth.mgr_db.getAllMgr()
        for mgr_data in mgr_datas:
            print(f'''
____________________________________________
manager id : {mgr_data[0]}                |
manager name : {mgr_data[1]}              |  
manager email : {mgr_data[2]}             |       
___________________________________________|''')
        adminMainMenu()

    elif Choice == 3 :
        managerPromotion()
    elif Choice == 4 :
        pass
    elif Choice == 5 :
        admin_services.seeMgrReq(admin_auth)
        adminMainMenu()
    elif Choice == 6 :
        pass
    elif Choice == 7 :
        pass
    elif Choice == 8 :
        return
    else:
        print("Enter the vaild option")
        adminMainMenu()


