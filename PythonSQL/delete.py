import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'python'
)

mycursor = mydb.cursor()

### DELETE TABELA ###
print('DELETE CLIENTE')
sql = "DELETE FROM cliente WHERE idCliente = '5'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')