from flask import Flask, render_template, Response, request
import serial
import time
import serial.tools.list_ports
from random import randint
from data.funcoes import SensorIV
from turbo_flask import Turbo

app = Flask(__name__)
turbo = Turbo(app)

sensor =[
    SensorIV(valor="0")
]

def lista_coms():

    portas_encontradas = serial.tools.list_ports.comports()
    print("\nPortas COM encontradas: ")
    for item in portas_encontradas:
        print(str(item))
    print("\n")

    return portas_encontradas

# Encontra a porta COM do Raspberry Pi Pico
def encontra_rasp(portas_encontradas):

    for porta in portas_encontradas:
        if "serial" in str(porta).lower():
            porta_rasp = str(porta)[:4]
            print(f"Raspberry Pi Pico encontrado na porta: {porta_rasp}")
            return porta_rasp

    print("Raspberry Pi Pico não encontrado.")

    return None

# Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
def conecta_serial(porta_com, taxa_transmissao, tempo_espera):

    comunicacao_serial = serial.Serial(porta_com, taxa_transmissao, timeout = tempo_espera)

    return comunicacao_serial

# Realiza todo o processo de conexao ate o rasp pela chamada de outras funcoes
def processo_conexao(taxa_de_transmissao_comunicacao, tempo_de_espera_conexao):
	portas_com = lista_coms() # Lista todas as portas COM
	porta_rasp = encontra_rasp(portas_com) # Encontra a porta COM do Raspberry Pi Pico
	comunicacao_serial = conecta_serial(porta_rasp, taxa_de_transmissao_comunicacao,tempo_de_espera_conexao) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
	return comunicacao_serial

taxa_transmissao = 115200 # bits por segundo
tempo_espera = 2 # segundos

resposta_para_tudo = processo_conexao(taxa_transmissao, tempo_espera)


def ledOn():
    resposta_para_tudo.write(str('1').encode() + b"\n")
    
def ledOff():
	resposta_para_tudo.write(str('0').encode() + b"\n")

def disconnect():
	resposta_para_tudo.close()

@app.route('/')
def index():
    return render_template('index.html', sensor=sensor)

@app.route('/get-value')
def get_value():
    value = resposta_para_tudo.readline().decode('utf-8')
    valor = value.strip()
    return {'value': valor}

if __name__ == "__main__":
    app.run()
