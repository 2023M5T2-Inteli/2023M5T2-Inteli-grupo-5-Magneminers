from flask import Flask, render_template, request, redirect
from data.funcoes import Evento, Posicao

posicoes =[
    Posicao(x="100", y="100", z="100", r="100", j1="100", j2="100", j3="100", j4="100")
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", posicoes=posicoes)

@app.route("/oi")
def teste():
    return render_template("cadastrar.html")

@app.route('/cima', methods=["POST"])
def enviar_cima():
    posicoesnovas = Posicao(
        y = request.form["C"],
        x = posicoes[(len(posicoes) - 1)].x,
        z = posicoes[(len(posicoes) - 1)].z,
        r = posicoes[(len(posicoes) - 1)].r,
        j1 = posicoes[(len(posicoes) - 1)].j1,
        j2 = posicoes[(len(posicoes) - 1)].j2,
        j3 = posicoes[(len(posicoes) - 1)].j3,
        j4 = posicoes[(len(posicoes) - 1)].j4
    )
    posicoes.append(posicoesnovas)
    return redirect("/")

@app.route('/esquerda', methods=["POST"])
def enviar_esquerda():
    posicoesnovas = Posicao(
        y = posicoes[(len(posicoes) - 1)].y,
        x = request.form["E"],
        z = posicoes[(len(posicoes) - 1)].z,
        r = posicoes[(len(posicoes) - 1)].r,
        j1 = posicoes[(len(posicoes) - 1)].j1,
        j2 = posicoes[(len(posicoes) - 1)].j2,
        j3 = posicoes[(len(posicoes) - 1)].j3,
        j4 = posicoes[(len(posicoes) - 1)].j4
    )
    posicoes.append(posicoesnovas)
    return redirect("/")

@app.route('/direita', methods=["POST"])
def enviar_direita():
    posicoesnovas = Posicao(
        y = posicoes[(len(posicoes) - 1)].y,
        x = request.form["D"],
        z = posicoes[(len(posicoes) - 1)].z,
        r = posicoes[(len(posicoes) - 1)].r,
        j1 = posicoes[(len(posicoes) - 1)].j1,
        j2 = posicoes[(len(posicoes) - 1)].j2,
        j3 = posicoes[(len(posicoes) - 1)].j3,
        j4 = posicoes[(len(posicoes) - 1)].j4
    )
    posicoes.append(posicoesnovas)
    return redirect("/")

@app.route('/baixo', methods=["POST"])
def enviar_baixo():
    posicoesnovas = Posicao(
        y = request.form["B"],
        x = posicoes[(len(posicoes) - 1)].x,
        z = posicoes[(len(posicoes) - 1)].z,
        r = posicoes[(len(posicoes) - 1)].r,
        j1 = posicoes[(len(posicoes) - 1)].j1,
        j2 = posicoes[(len(posicoes) - 1)].j2,
        j3 = posicoes[(len(posicoes) - 1)].j3,
        j4 = posicoes[(len(posicoes) - 1)].j4
    )
    posicoes.append(posicoesnovas)
    return redirect("/")

@app.route('/reset', methods=["POST"])
def enviar_reset():
    posicoesnovas = Posicao(
        y = 100,
        x = 100,
        z = 100,
        r = 100,
        j1 = 100,
        j2 = 100,
        j3 = 100,
        j4 = 100
    )
    posicoes.append(posicoesnovas)
    return redirect("/")

app.run(host='0.0.0.0', port= 3000, debug=True)