import serial 
import serial.tools.list_ports
from time import sleep

# Lista todas as portas COM, uma delas é o Raspberry Pi Pico
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

tempo_espera = 2
taxa_transmissao = 115200

portas_com = lista_coms() # Lista todas as portas COM
porta_rasp = encontra_rasp(portas_com) # Encontra a porta COM do Raspberry Pi Pico
comunicacao_serial = conecta_serial(porta_rasp, taxa_transmissao, tempo_espera) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está

while True:
    #Leitura do Sensor infravermelho conectado no Raspberry Pico W
    valor_distancia = comunicacao_serial.readline() # Realiza a leitura de um pacote de informaçãoes via serial
    print(valor_distancia.decode("UTF-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto