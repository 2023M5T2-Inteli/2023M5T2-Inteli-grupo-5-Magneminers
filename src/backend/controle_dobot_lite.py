# Importação das bibliotecas necessárias para o script
from time import sleep
from enum import Enum
import serial.tools.list_ports
import serial
import pydobot

# Configurações de comunicação
TEMPO_ESPERA_CONEXAO = 2 # segundos
TAXA_TRANSMISSAO_COMUNICACAO = 115200 # bits por segundo

# Enumeração das ações do eletroímã
class AcoesEletroima(Enum):
    LIGAR = 1
    DESLIGAR = 0

# Enumeração das posições do Dobot Magician Lite
class Poses(Enum):
    ALTURA_SUBIDA = 70
    ALTURA_BANDEJA = 30

    X_BANDEJA_A = 20
    Y_BANDEJA_A = -108
    DESLOCAMENTO_X_BANDEJA_A = 42
    DESLOCAMENTO_Y_BANDEJA_A = -21

    X_BANDEJA_B = 67
    Y_BANDEJA_B = -5
    DESLOCAMENTO_X_BANDEJA_B = 50
    DESLOCAMENTO_Y_BANDEJA_B = 0

    X_BANDEJA_C = 30
    Y_BANDEJA_C = 108
    DESLOCAMENTO_X_BANDEJA_C = 42
    DESLOCAMENTO_Y_BANDEJA_C = 21

# Configurações do ensaio
class Ensaio(Enum):
    NUMERO_VARRERUDAS_AMOSTRA = 5
    NUMERO_CICLOS_ENSAIO = 10

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

# Envia um comando para o Raspberry Pi Pico controlar o eletroímã
def controle_eletroima(com_serial_ima, estado):
    com_serial_ima.write(str(estado).encode() +b"\n")
    return None

# Configura a comunicação do eletroíma e do braço
def setup(taxa_transmissao_comunicacao, tempo_espera_conexao):
    print("Listando portas COM... \n")
    portas_com = lista_coms() # Lista todas as portas COM
    print("Encontrando porta COM do Raspberry Pi Pico... \n")
    porta_rasp = encontra_rasp(portas_com) # Encontra a porta COM do Raspberry Pi Pico
    print("Conectando com o Raspberry Pi Pico... \n")
    com_rasp = conecta_serial(porta_rasp, taxa_transmissao_comunicacao, timeout=tempo_espera_conexao) # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
    print("Conectando com o Dobot Magitian Lite... \n")
    braco_dobot = pydobot.Dobot(port=portas_com[0], verbose=False) # Cria um objeto que controla o braço
    
    return com_rasp, braco_dobot

# Faz com que o braço vá até a bandeja, abeixe sua ponta de amostragem, varra a bandeja n vezes e suba novamente
def percorre_bandeja(x0, y0, z0, braco_dobot, x_bandeja, y_bandeja, deslocamento_x_bandeja,     deslocamento_y_bandeja, altura_subida, altura_bandeja, n_varreduras, com_eletroima, estado_eletroima):

    # Ir até a bandeja de amostragem
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + altura_subida,
                        wait = True)  
    
    # Controla eletroíma
    controle_eletroima(com_eletroima, estado_eletroima)

    # Descer até a amostra
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + Poses.ALTURA_BANDEJA.value,
                        wait = True)  
    
    # Percorre bandeja n vezes
    for i in range(n_varreduras):
        braco_dobot.move_to(x0 + x_bandeja + deslocamento_x_bandeja, 
                            y0 + y_bandeja + deslocamento_y_bandeja,
                            z0 + altura_bandeja,
                            wait = True) 
        
        braco_dobot.move_to(x0 + x_bandeja, 
                            y0 + y_bandeja,
                            z0 + altura_bandeja,
                            wait = True)  
        
        print("Varredura ", i, " de ", n_varreduras)

    # Suspender braço acima da bandeja para ir para a próxima
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + altura_subida,
                        wait = True)  
    
    return None
    
# Prepara o braço robótico e o eletroíma para o ensaio
def despertar(taxa_transmissao, tempo_espera, altura_subida):
    com_dispositivo, braco_robotico = setup(taxa_transmissao,  tempo_espera)
    (x0, y0, z0, r0, j10, j20, j30, j40) = braco_robotico.pose() 
    braco_robotico.move_to(x0, y0, z0 + altura_subida, r0, wait=True)

    return com_dispositivo, x0, y0, z0, braco_robotico

# Desliga o braço robótico e o eletroíma
def adormecer(braco_robotico, com_dispositivo):
    braco_robotico.close()
    com_dispositivo.close()

    return None

if __name__ == "__main__":

    # Inicializa o ensaio
    maganalyzer, x0, y0, z0, com_eletroima = despertar(TAXA_TRANSMISSAO_COMUNICACAO, TEMPO_ESPERA_CONEXAO, Poses.ALTURA_SUBIDA.value)

    # Executa o ensaio
    for i in range(Ensaio.NUMERO_CICLOS_ENSAIO.value):

        # Amostra material
        percorre_bandeja(x0, y0, z0, 
                        maganalyzer, 
                        Poses.X_BANDEJA_A.value,
                        Poses.Y_BANDEJA_A.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_A.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_A.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        com_eletroima, 
                        AcoesEletroima.LIGAR.value)

        # Lava material
        percorre_bandeja(x0, y0, z0, 
                        maganalyzer, 
                        Poses.X_BANDEJA_B.value,
                        Poses.Y_BANDEJA_B.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_B.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_B.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        com_eletroima, 
                        AcoesEletroima.LIGAR.value)

        # Deposita material
        percorre_bandeja(x0, y0, z0, 
                        maganalyzer, 
                        Poses.X_BANDEJA_C.value,
                        Poses.Y_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_C.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        com_eletroima, 
                        AcoesEletroima.DESLIGAR.value)
        
    # Finaliza o ensaio
    adormecer(maganalyzer, com_eletroima)