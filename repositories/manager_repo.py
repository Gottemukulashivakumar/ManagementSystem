from db_pool.connection import connect,cursor

class managerDb:
    def getAllMgr(self):
        query = 'select * from user where is_manager=%s'
        cursor.execute(query,(1,))
        datas = cursor.fetchall()
        return datas
    def getEmp():
        query = 'select * from user where mgr_id = %s'
        cursor.execute(query,(id,))
        datas = cursor.fetchall()
        return datas