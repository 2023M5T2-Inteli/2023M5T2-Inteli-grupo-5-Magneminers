# Importando as bibliotecas necessarias para o script, inculindo funções em outros scripts
from flask import Flask, render_template, Response, request, redirect
from conexao import resposta_para_tudo
from joystick import coordenadas, coordenadas_e
import pymongo
from pymongo import MongoClient
from data.robot_singleton import RobotSingleton


# Inicializa o flask
app = Flask(__name__)

# Declaração de variáveis globais
global ensaio, ensaiof, id_ensaio

# Inicializa o banco de dados MongoDB
cluster = MongoClient("mongodb+srv://Gabi-Barretto:DarthVader01@modulo5.ftovxoa.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Ensaios"]
collection = db["Ensaios"]


# Função para criar ensaio no banco de dados
def criar_ensaio(e, cic, vrr):
    collection.insert_one({"_id": e, "cic": cic, "vrr": vrr})
    return print("Ensaio criado com sucesso")

# Função para atualizar as coordenadas do ensaio no banco de dados
def update_ensaio_b1(x, y, z, e):
    collection.update_one({"_id": e}, {"$set": {"x1": x, "y1": y, "z1": z}})
    return print("B1 Atualizado")

def update_ensaio_b2(x, y, z, e):
    collection.update_one({"_id": e}, {"$set":  {"x2": x, "y2": y, "z2": z}})
    return print("B2 Atualizado")

def update_ensaio_b3(x, y, z, e):
    collection.update_one({"_id": e}, {"$set":  {"x3": x, "y3": y, "z3": z}})
    return print("B3 Atualizado")

def update_ensaio_b1_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x1_e": x, "y1_e": y}})
    return print("B1_e Atualizado")

def update_ensaio_b2_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x2_e": x, "y2_e": y}})
    return print("B2_e Atualizado")

def update_ensaio_b3_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x3_e": x, "y3_e": y}})
    return print("B3_e Atualizado")

# Função para encontrar o ensaio no banco de dados
def encontra_ensaio(id_ensaio): #Precisa substituir o id por um request.form 
    ensaio_pronto = collection.find_one({"_id": id_ensaio}) 
    print(type(ensaio_pronto))
    return ensaio_pronto

# Declaração da variável ensaio para evitar conflitos
ensaio = None

# Declaração da rota inicial, com a página home.html
@app.route("/")
def index():
    return render_template("home.html", ensaio=ensaio)

# Funções para acionar e desacionar o eletroímã e o led da solução
def ledOn():
    resposta_para_tudo.write(str('1').encode() + b"\n")
    
def ledOff():
	resposta_para_tudo.write(str('0').encode() + b"\n")

def disconnect():
	resposta_para_tudo.close()

# Rota e funcao para acionar e desacionar o eletroímã e o led da solução	
@app.route("/led", methods=['GET', 'POST'])
def led():
	if request.method == 'POST':
		if 'on' in request.form.to_dict():
			ledOn()
		if 'off' in request.form.to_dict():
			ledOff()
		if 'dis' in request.form.to_dict():
			disconnect()

	return redirect("/")

# Rota e funcao para criar o ensaio
@app.route("/criar", methods=["POST"])
def cria_ensaio():
	global ensaio

	ensaio = request.form["ensaio"]

	criar_ensaio(ensaio, request.form["cic"], request.form["vrr"])
	return redirect("/")

# Rotas e funções para complementar o ensaio com as coordenadas
@app.route("/b1", methods=["POST"])
def b1():
	x, y, z = coordenadas()
	update_ensaio_b1(x, y, z, ensaio)
	return redirect("/")

@app.route("/b2", methods=["POST"])
def b2():
	x, y, z = coordenadas()
	update_ensaio_b2(x, y, z, ensaio)
	return redirect("/")
	
@app.route("/b3", methods=["POST"])
def b3():
	x, y, z = coordenadas()
	update_ensaio_b3(x, y, z, ensaio)
	return redirect("/")
	
@app.route("/b1_e", methods=["POST"])
def b1_e():
	x, y = coordenadas_e()
	update_ensaio_b1_e(x, y, ensaio)
	return redirect("/")
	
@app.route("/b2_e", methods=["POST"])
def b2_e():
	x, y = coordenadas_e()
	update_ensaio_b2_e(x, y, ensaio)
	return redirect("/")
	
@app.route("/b3_e", methods=["POST"])
def b3_e():
	x, y = coordenadas_e()
	update_ensaio_b3_e(x, y, ensaio)    
	return redirect("/")
    
# Rota e função para iniciar o ensaio
@app.route("/finalizar", methods=["POST"])
def iniciar_ensaio():	

	id_ensaio = request.form["id_ensaio"]
	
	ensaiof = encontra_ensaio(id_ensaio)

	# Inicializa o singleton e seta o ensaio para ser buscado no banco de dados
	robot = RobotSingleton()
	robot.set_ensaio_id(ensaiof)
	print(robot.get_ensaio_id())

	with open("src/controle_dobot_lite.py") as f:
		exec(f.read())
	return redirect("/")


if __name__ == "__main__":
    app.run()