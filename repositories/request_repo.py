from db_pool.connection import connect,cursor

class RequestDb:
    def createRequest(self,mgr_id):
        query = 'insert into mgr_id(req_by) values(%s)'
        values = (mgr_id,)
        cursor.execute(query,values)
        cursor.commit()

    def getAllReq(self):
        query = 'select * from mgr_req'
        cursor.execute(query)
        datas = cursor.fetchall()
        return datas
    
    def deleteReq(self,id):
        query = 'delete from mgr_req where req_id '
        cursor.execute(query,(id))
        connect.commit()
        cursor.execute(query)
    

req_db = RequestDb()
# req_db.createRequest(7)