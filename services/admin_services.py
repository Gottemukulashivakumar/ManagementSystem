def seeMgrReq(admin_obj):
    datas = admin_obj.req_db.getAllReq()
    emp_datas = admin_obj.db.getEmpwoMgr()
    if  datas:
        print(f'request_id {data[0]}: manager id with {data[1]} requesting employee for team')
        for data in datas:

            choice = int(input('''press 1 for assign employee
                           press 2 for cancel request 
                           press 3 for cgo to main menu
                           Enter the option : '''))
        if choice == 1 :
            print('employee without manager')
            for emp_data in emp_datas:
                print(f'''
employee id:{emp_data[0]}
employee name :{emp_data[1]}''')
            req_id = int(input("Enter request id :"))
            mgr_id = int(input('Enter manager id:'))
            emp_id = int(input ('Enter emp id:'))
            admin_obj.db.updateMgr(emp_id,mgr_id)
            admin_obj.req_db.deleteReq(id)
            print('request rejection successfully!!!!!')
            seeMgrReq(admin_obj)
        elif choice == 2:
            req_id = int(input('Enter request id to reject:'))
            admin_obj.req_db.deleteReq(req_id)
            print('request rejection successfully!!!!!')
            seeMgrReq(admin_obj)

        elif choice == 3:
            return 
    
        else :
            print("Entered values id incorrect ")
            seeMgrReq()
    else:
        print("-----no request-----")
        return



