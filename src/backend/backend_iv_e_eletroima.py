#Importamos as bibliotecas necessárias para que o programa consiga rodar suas dependências tranquilamente
import serial
import serial.tools.list_ports
import time
from random import randint


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

# Inicializa o loop do python de requisição/envio a Serial do Raspberry caso seja conectado e tudo a cima de certo para comecar a manipulacao do eletroima
while True:
    
    sensor_requisitado = input("Sensor: ")
    
    if sensor_requisitado == "ec":
        # Espera o input do usuario para mudar o estado do eletroima
        estado_eletroima = input("Estado: ")
        # Transforma em string para depois ser codificado e ser enviado ao Raspberry 
        estado_eletroima = str(estado_eletroima)
        # Apresenta o número de estado no terminal do Python
        print(estado_eletroima)
        
        # Valor do PWM editado a partir do Input do usuario.
        valor_pwm_eletroima = input("Valor PWM: ")
        valor_pwm_eletroima = str(valor_pwm_eletroima)
        #Junta ambos em uma string
        info_eletroima = str(sensor_requisitado) + "," + estado_eletroima + "," + valor_pwm_eletroima
        print(info_eletroima)
        # Codifica o número para que consiga ser enviado ao Raspberry.
        eletroima_encode = info_eletroima.encode()

        # Envia o número de estado para o Raspberry através da linha de comando que definiu as suas propriedades, escrevendo através da serial
        comunicacao_serial.write(eletroima_encode + b"\n") # Escreve o número na serial para o Raspberry receber e fazer a manipulacao atraves da Ponte H
        time.sleep(1) # Espera um segundo e repete o loop
        
    elif sensor_requisitado == "iv":
        
        # Para evitar erros no raspberry ao realizar o split para transformarmos os dados em uma lista, temos que definir dados para o Infravermelho tambem...
        estado_iv = "1"
        valor_pwm_iv = "100"
        
        info_iv = str(sensor_requisitado) + "," + estado_iv + "," + valor_pwm_iv
        print(info_iv)
        
        iv_encode = info_iv.encode()
        
        comunicacao_serial.write(iv_encode + b"\n")
        #Leitura do Sensor infravermelho conectado no Raspberry Pico W
        valor_distancia = comunicacao_serial.readline() # Realiza a leitura de um pacote de informaçãoes via serial:
        print(valor_distancia.decode("utf-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto