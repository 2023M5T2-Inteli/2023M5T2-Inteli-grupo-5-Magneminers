# Import all the libraies to make the code bellow work
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
    comunicacao_serial = serial.Serial(porta_com, taxa_transmissao, timeout=tempo_espera)
    return comunicacao_serial

def setup(taxa_transmissao_comunicacao, tempo_espera_conexao):
    print("Listando portas COM... \n")
    portas_com = lista_coms()                                   # Lista todas as portas COM
    print("Encontrando porta COM do Raspberry Pi Pico... \n")
    porta_rasp = encontra_rasp(portas_com)   
    porta_rasp = "COM7"                   # Encontra a porta COM do Raspberry Pi Pico
    print("Conectando com o Raspberry Pi Pico... \n")
    com_rasp = conecta_serial(porta_rasp, taxa_transmissao_comunicacao, tempo_espera_conexao)           # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está

    return com_rasp

# Envia um comando para o Raspberry Pi Pico controlar o eletroímã
def envia_serial(com_serial, mensagem):
    com_serial.write(str(mensagem).encode() + b"\n")

    return None

def le_balanca(com_recebimento):
    for i in range(3):
        envia_serial(com_recebimento, "b")
        mensagem_recebida = com_recebimento.readline().decode().strip()
    return mensagem_recebida

def teste_geral(com_serial, n_repeticoes):
    com_serial.write(("t," + str(n_repeticoes)).encode() + b"\n")


taxa_transmissao = 115200
tempo_espera = 1

if __name__ == "__main__":

    com_raspberry = setup(taxa_transmissao, tempo_espera)

    while True:

        comando = input("Digite um comando: ")
        envia_serial(com_raspberry, comando)
       
        dado_balanca = le_balanca(com_raspberry)
        print("Dado balanca: ", dado_balanca)
        
        print()
        