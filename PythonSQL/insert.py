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
telefone = '(11)5452-3211'
cidade = 'São Paulo'

### INSERT TABELA ###
print('INSERIR CLIENTE')
sql = "INSERT INTO cliente (Nome, Telefone, Cidade) values (%s, %s, %s)"
val = (cliente, telefone, cidade)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record(s) insert')