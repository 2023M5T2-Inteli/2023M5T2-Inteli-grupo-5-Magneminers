#Importamos as bibliotecas necessárias para que o programa consiga rodar suas dependências tranquilamente

import serial.tools.list_ports
import time
from random import randint

#Definimos as variáveis de configuração do Raspberry
tempo_espera = 2 # Tempo máximo de espera de conexão ao raspberry em segundos
taxa_transmissao = 115200 # Taxa BAUD de transmissao de serial que o Raspberry se comunica

# Funcao com o objetivo de listar todas as portas que temos conectadas no nosso computador para ficar mais fácil de identificar
# qual a porta atual do Raspberry, podendo variar entre COM3-5
def find_coms(): 

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found: # Lista todas as portas encontradas
        print(str(item))

    return ports_found # Retorna todas as portas encontradas

find_coms() # Executa a função escrita a cima

# Linha de comando definindo as propriedades de comunicação via serial do Python ao Raspberry utilizando a biblioteca
# Serial e as variáveis escritas a cima
comunicacao_serial = serial.Serial("COM7", taxa_transmissao, timeout = tempo_espera)

# Inicializa o loop do python de requisição/envio a Serial do Raspberry caso seja conectado e tudo a cima de certo para comecar a manipulacao do eletroima
while True:

    # Espera o input do usuario para mudar o estado do eletroima
    estado_eletroima = input("Estado: ")
    # Transforma em string para depois ser codificado e ser enviado ao Raspberry 
    estado_eletroima = str(estado_eletroima)
    # Apresenta o número de estado no terminal do Python
    print(estado_eletroima)
    # Codifica o número para que consiga ser enviado ao Raspberry.
    estado_eletroima_encode = estado.encode()

    # Envia o número de estado para o Raspberry através da linha de comando que definiu as suas propriedades, escrevendo através da serial
    comunicacao_serial.write(estado_eletroima_encode + b"\n") # Escreve o número na serial para o Raspberry receber e fazer a manipulacao atraves da Ponte H
    time.sleep(1) # Espera um segundo e repete o loop