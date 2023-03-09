# Importação das bibliotecas necessárias

import serial.tools.list_ports
from time import sleep

tempo_espera = 2 # Define o tempo de espera da comunicação serial como 2 segundos
taxa_transmissao = 115200 # Define a taxa de transmissão

# A função abaixo busca e exibe as portas COM conectadas ao dispositivo

def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

# A função abaixo busca e exibe a porta COM do microcontrolador Raspberry Pi Pico W

def encontra_rasp(portas_encontradas):

    for porta in portas_encontradas:
        if "serial" in str(porta).lower():
            porta_rasp = str(porta)[:4]
            print(f"Raspberry Pi Pico encontrado na porta: {porta_rasp}")
            return porta_rasp
        else:
            print("Raspberry Pi Pico não encontrado.")

    return None

# A função abaixo abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico W está

def conecta_serial(porta_com, taxa_transmissao, tempo_espera):

    comunicacao_serial = serial.Serial(porta_com, taxa_transmissao, timeout = tempo_espera)

    return comunicacao_serial

portas_com = find_coms() # Executa a função que busca as portas conectadas
porta_rasp = encontra_rasp(portas_com) # Encontra a porta COM do Raspberry Pi Pico
comunicacao_serial = conecta_serial(porta_rasp, taxa_transmissao, tempo_espera) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está

while True:

    valor_loadcell = comunicacao_serial.readline() # Realiza a leitura dos dados do sensor de carga via serial
    print(valor_loadcell.decode("UTF-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto
