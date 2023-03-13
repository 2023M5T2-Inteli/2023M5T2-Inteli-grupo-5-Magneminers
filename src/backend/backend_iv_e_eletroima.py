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

# Realiza todo o processo de conexao ate o rasp pela chamada de outras funcoes
def processo_conexao(taxa_de_transmissao_comunicacao, tempo_de_espera_conexao):
    
    portas_com = lista_coms() # Lista todas as portas COM
    porta_rasp = encontra_rasp(portas_com) # Encontra a porta COM do Raspberry Pi Pico
    comunicacao_serial = conecta_serial(porta_rasp, taxa_de_transmissao_comunicacao, tempo_de_espera_conexao) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
    return comunicacao_serial
    
def enviar_info_ao_rasp(sensor, estado, valor_pwm):
    #Junta todos em uma string
    info_sensor = str(sensor) + "," + str(estado) + "," + str(valor_pwm)
    print(info_sensor)
    # Codifica o número para que consiga ser enviado ao Raspberry.
    sensor_encode = info_sensor.encode()
    # Envia o número de estado para o Raspberry através da linha de comando que definiu as suas propriedades, escrevendo através da serial
    comunicacao_serial.write(sensor_encode + b"\n") # Escreve o número na serial para o Raspberry receber e fazer a manipulacao atraves da Ponte H.

# Configurações de comunicação
taxa_transmissao = 115200 # bits por segundo
tempo_espera = 2 # segundos

# variaveis especiais para deixar o codigo mais robusto e evitar erros
if __name__ == "__main__":
    
    processo_conexao(taxa_transmissao, tempo_espera)

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
            
            enviar_info_ao_rasp(sensor_requisitado, estado_eletroima, valor_pwm_eletroima)
            time.sleep(1) # Espera um segundo e repete o loop

        elif sensor_requisitado == "iv":

            # Para evitar erros no raspberry ao realizar o split para transformarmos os dados em uma lista, temos que definir dados para o Infravermelho tambem, sao os numeros padroes porem que fazem grandes diferencas pra gente nesse resultado em especifico(afinal, se ele estiver desligado por exemplo, como vamos pegar os dados de distancia?)...
            estado_iv = "1"
            valor_pwm_iv = "100"

            enviar_info_ao_rasp(sensor_requisitado, estado_iv, valor_pwm_iv)
            
            #Leitura do Sensor infravermelho conectado no Raspberry Pico W
            valor_distancia = comunicacao_serial.readline() # Realiza a leitura de um pacote de informaçãoes via serial(a principio, a distancia por ser o sensor IV):
            print(valor_distancia.decode("utf-8")) # Exibe a string que foi enviada pelo Raspberry Pi Pico decodificada como texto
            time.sleep(1) # Espera um segundo e repete o loop
