def viewAllEmp(mgr_id,mgr_obj):
    datas = mgr_obj.mgr_db.getEmp(mgr_id)
    print("YOUR TEAM")
    for data in datas:
        print(F'''
Employee id :{data[0]}
EMPLOYEE name :{data[1]}
Employee email : {data[2]}''')
    else :
        print("no employee assigned yet!!!!!")
        mgrOption(mgr_id,mgr_obj)

def mgrRequest (mgr_obj,mgr_id):
    en = input("press ENTER to request a employee  for the team")
    mgr_obj.req_db.createRequest(mgr_id)
    print('request sent to admin successfully')
    


def mgrOption(mgr_id,mgr_obj):
        print('''enter 1 for request employee from admin
enter 2 for go back to mainmenu''')
        choice = int(input('Enter your option'))
        if choice == 1:
            mgrRequest(mgr_id,mgr_obj)
        elif choice == 2:
            return
        else :
             print("enter vaild option")

    