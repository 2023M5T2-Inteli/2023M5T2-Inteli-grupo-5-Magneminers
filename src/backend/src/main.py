from flask import Flask, render_template, Response, request, redirect
from data.posicoes import Posicao, Ensaio
from conexao import resposta_para_tudo
from joystick import coordenadas


posicoes =[
    # Posicao(x1 = "0", y1 = "0", z1 = "0", xd1 = "0", yd1 = "0", x2 = "0", y2 = "0", z2 = "0", xd2 = "0", yd2 = "0", x3 = "0", y3 = "0", z3 = "0", xd3 = "0", yd3 = "0", ptc = "0", vrr = "0", cic = "0")
]

ensaios = [
	
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

	return redirect("/")

@app.route("/criar", methods=["POST"])

def gerar_coordenada():

    #posicao = Posicao(
        # x1=request.form["x1"],
        # y1=request.form["y1"],
        # z1=request.form["z1"],

        # xd1=request.form["xd1"],
        # yd1=request.form["yd1"],

        # x2=request.form["x2"],
        # y2=request.form["y2"],
        # z2=request.form["z2"],

        # xd2=request.form["xd2"],
        # yd2=request.form["yd2"],

        # x3=request.form["x3"],
        # y3=request.form["y3"],
        # z3=request.form["z3"],

        # xd3=request.form["xd3"],
        # yd3=request.form["yd3"],

        # ptc=request.form["ptc"],
        # vrr=request.form["vrr"],
        # cic=request.form["cic"]
        
    #)

    x0, y0, z0 = coordenadas()

    posicao = Posicao(
        x1=x0,
        y1=y0,
        z1=z0
    )

    global posicoes
    
    posicoes.append(posicao)

    return redirect("/")

@app.route("/finalizar", methods=["POST"])
def gerar_ensaio():	
	
    ensaioo = Ensaio( 
        bd1=request.form["bd1"],
        bd2=request.form["bd2"],
        vrr=request.form["vrr"],
        cic=request.form["cic"]
    )
    
    global ensaios
    ensaios.append(ensaioo)

    with open("src\controle_dobot_lite.py") as f:
       exec(f.read())
    
    return redirect("/")


if __name__ == "__main__":
    app.run()