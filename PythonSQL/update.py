import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'python'
)

mycursor = mydb.cursor()

### Variaveis ###
cliente = 'Jessica'
telefone = '(11)98542-4345'
cidade = 'São Paulo'
IdCliente = '7'

### UPDATE TABELA ###
print('ATUALIZAR CLIENTE')
sql = "UPDATE cliente SET Telefone = %s WHERE IdCliente = %s"
val = (telefone, IdCliente)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) update')