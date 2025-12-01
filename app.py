from flask import Flask, render_template
import json
from flask import flash, redirect
from utils import db
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')


conexao = f"mysql+pymysql://{db_usuario}:{db_password}@{db_host}:{db_port}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/compras', methods=['POST'])
def compras():
    #itens = ['Arroz', 'Feijão', 'Macarrão','Açúcar', 'Farinha', 'Tomate', 'Cebola', 'Alho']
    itens = request.form.getlist('item')
    return render_template('compras.html', itens=itens)

@app.route('/tarefa'):
    tarefa = tarefa.query.all()
    return render_template(tarefa.html, tarefas=tarefas)

@app.route("/create", methods=['POST'])
def create_tarefa():
    descricao = request.form['descricao']
    new_tarefa = Tarefa(descricao=descricao)
    db.session.add(new_tarefa)
    db.session.commit()#SEMPRE DAR COMMIT
    return redirect(url_for('tarefa.html'))

@app.route("/update/<int:tarefa_id>", methods=['POST'])
def update_tarefa(tarefa_id):
    tarefa_obj = Tarefa.query.get(tarefa_id)
    if tarefa_obj:
        tarefa_obj.descricao = request.form['descricao']
        db.session.commit()
    return redirect(url_for('tarefa.html'))

@app.route("/delete/<int:tarefa_id>", methods=['POST'])
def delete_tarefa(tarefa_id):
    tarefa_obj = Tarefa.query.get(tarefa_id)
    if tarefa_obj:
        db.session.delete(tarefa_obj)
        db.session.commit()
    return redirect(url_for('tarefa.html'))

if __name__ == "__main__":
    app.run()