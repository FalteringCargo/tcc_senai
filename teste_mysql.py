import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco_de_dados"
)

print("Conectado com sucesso!")