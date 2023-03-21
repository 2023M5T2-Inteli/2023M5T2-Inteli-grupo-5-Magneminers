from flask import Flask, render_template, Response, request, redirect
from data.mongodb import criar_ensaio, update_ensaio_b1, update_ensaio_b2, update_ensaio_b3, update_ensaio_b1_e, update_ensaio_b2_e, update_ensaio_b3_e, encontra_ensaio
from conexao import resposta_para_tudo
from joystick import coordenadas, coordenadas_e
#from controle_dobot_lite import start

app = Flask(__name__)

ensaio = None

@app.route("/")
def index():
    return render_template("home.html", ensaio=ensaio)

def ledOn():
    resposta_para_tudo.write(str('1').encode() + b"\n")
    
def ledOff():
	resposta_para_tudo.write(str('0').encode() + b"\n")

def disconnect():
	resposta_para_tudo.close()

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

@app.route("/criar", methods=["POST"])
def cria_ensaio():
	global ensaio

	ensaio = request.form["ensaio"]

	criar_ensaio(ensaio, request.form["cic"], request.form["vrr"])
	return redirect("/")


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
    

@app.route("/finalizar", methods=["POST"])
def iniciar_ensaio():	

	# start(ensaio)

	with open("src\controle_dobot_lite.py") as f:
		exec(f.read())
	return redirect("/")


if __name__ == "__main__":
    app.run()