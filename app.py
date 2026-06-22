from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    
    app.run(debug=True , host='0.0.0.0')

import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco_de_dados"
)

print("Conectado com sucesso!")