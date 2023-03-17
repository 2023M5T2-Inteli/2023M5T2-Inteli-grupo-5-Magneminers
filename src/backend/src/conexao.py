import serial
import serial.tools.list_ports
import pydobot


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
    porta_dobot = portas_com[2].device # Encontra a porta COM do Dobot Magician Lite
    comunicacao_serial = conecta_serial(porta_rasp, taxa_de_transmissao_comunicacao,tempo_de_espera_conexao) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
    print("Conectando com o Dobot Magitian Lite... \n")
    braco_dobot = pydobot.Dobot(port=porta_dobot, verbose=False) # Cria um objeto que controla o braço
    return comunicacao_serial, braco_dobot

taxa_transmissao = 115200 # bits por segundo
tempo_espera = 2 # segundos

resposta_para_tudo, dobot = processo_conexao(taxa_transmissao, tempo_espera)
