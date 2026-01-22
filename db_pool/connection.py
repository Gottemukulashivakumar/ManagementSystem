from mysql import connector

connect = connector.connect(
    user = 'root',
    password = 'root',
    host = 'localhost',
    database = 'management_db'
)

# if connect.is_connected():
#     print('successful')
# else:
#     print('not connected')

cursor = connect.cursor()
