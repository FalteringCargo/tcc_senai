from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/home')
def home():

    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco_de_dados",
    port=3306
    )

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtoss")
    consulta_banco = cursor.fetchall()

    return render_template('home.html', consulta_banco=consulta_banco)
@app.route('/devolucao_retirada')
def devolucao_retirada():
    return render_template('devolucao_retirada.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    
    app.run(debug=True , host='0.0.0.0')




print("Conectado com sucesso!")