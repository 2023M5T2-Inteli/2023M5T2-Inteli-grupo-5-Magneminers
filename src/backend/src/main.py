from flask import Flask, render_template, Response, request, redirect
import serial
import time
import serial.tools.list_ports
from random import randint
from data.posicoes import Posicao
from conexao import resposta_para_tudo

posicoes =[
    Posicao(x1 = "0", y1 = "0", z1 = "0", xd1 = "0", yd1 = "0", x2 = "0", y2 = "0", z2 = "0", xd2 = "0", yd2 = "0", x3 = "0", y3 = "0", z3 = "0", xd3 = "0", yd3 = "0", ptc = "0", vrr = "0", cic = "0")
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", posicoes=posicoes)

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

		#if request.form['off']:
		#	print('asdfdsafsdfasf')
	return redirect("/")


@app.route("/criar", methods=["POST"])
def criar_evento():
    posicao = Posicao(
        x1=request.form["x1"],
        y1=request.form["y1"],
        z1=request.form["z1"],

        xd1=request.form["xd1"],
        yd1=request.form["yd1"],

        x2=request.form["x2"],
        y2=request.form["y2"],
        z2=request.form["z2"],

        xd2=request.form["xd2"],
        yd2=request.form["yd2"],

        x3=request.form["x3"],
        y3=request.form["y3"],
        z3=request.form["z3"],

        xd3=request.form["xd3"],
        yd3=request.form["yd3"],

        ptc=request.form["z1"],
        vrr=request.form["z1"],
        cic=request.form["z1"]
    )

    global posicoes
    posicoes.append(posicao)
    return redirect("/")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 3000, debug=True)