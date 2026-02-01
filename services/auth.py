# module for login & signup for employee and admin

class AdminAuthentication:
    def __init__(self,db,mgr_db,req_db):
        self.db = db
        self.mgr_db = mgr_db
        self.req_db = req_db


class ManagerAuthentication:
    def __init__(self,db,req_db):
        self.mgr_db = db
        self.req_db = req_db

class EmployeeAuthentication:
    def __init__(self,db):
        self.db = db

    def createEmployee(self,e_name,e_email,password):
        # name = input('Enter ur name:')
        # email = input('Enter your email')
        # password = input('enter your password')
        # emp_auth.createEmployee(name,email,password)
        
        self_e_name = e_name
        self_e_email = e_email
        self_password = password
        self.db.createEmp(self_e_name,self_e_email,self_password)

    def empLogin(self,email):
        return self.db.searchEmp(email)