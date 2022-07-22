import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'python'
)

mycursor = mydb.cursor()

### CONSULTA TABELA ###
print('Consulta TABELA CLIENTE')
mycursor.execute('SELECT * FROM cliente')
myresult = mycursor.fetchall()
for line in myresult:
    print('Line: ', line)