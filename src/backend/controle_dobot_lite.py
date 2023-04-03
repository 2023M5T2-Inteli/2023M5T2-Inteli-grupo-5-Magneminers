# Importação das bibliotecas necessárias para o script
from enum import Enum
import serial.tools.list_ports
import serial
import pydobot
import pandas as pd

# Configurações de comunicação
TEMPO_ESPERA_CONEXAO = 2                    # segundos
TAXA_TRANSMISSAO_COMUNICACAO = 115200       # bits por segundo


# Enumeração das ações do eletroímã
class AcoesEletroima(Enum):
    LIGAR = "e,1,100,g"
    DESLIGAR = "e,0,100,r"


# Enumeração das posições do Dobot Magician Lite
class Poses(Enum):
    ALTURA_SUBIDA = 80
    ALTURA_BANDEJA = 25

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
    NUMERO_VARRERUDAS_AMOSTRA = 1
    NUMERO_CICLOS_ENSAIO = 4


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


# Envia um comando para o Raspberry Pi Pico controlar o eletroímã
def controle_eletroima(com_serial_ima, estado):
    com_serial_ima.write(str(estado).encode() + b"\n")
    return None

def le_balanca(com_recebimento):
    for i in range(3):
        controle_eletroima(com_recebimento, "b")
        mensagem_recebida = com_recebimento.readline().decode().strip()
    return mensagem_recebida


# Configura a comunicação do eletroíma e do braço
def setup(taxa_transmissao_comunicacao, tempo_espera_conexao):
    #print("Listando portas COM... \n")
    #portas_com = lista_coms()                                   # Lista todas as portas COM
    #print("Encontrando porta COM do Raspberry Pi Pico... \n")
    #porta_rasp = encontra_rasp(portas_com)                      # Encontra a porta COM do Raspberry Pi Pico
    #print("Conectando com o Raspberry Pi Pico... \n")
    com_rasp = conecta_serial("COM7", taxa_transmissao_comunicacao, tempo_espera_conexao)           # Abre um objeto de comunicação com a porta na qual o Raspberry Pi Pico está
    print("Conectando com o Dobot Magitian Lite... \n")
    #braco_dobot = pydobot.Dobot(port="COM7", verbose=False)      # Cria um objeto que controla o braço
    braco_dobot = pydobot.Dobot(port="COM5", verbose=False)
        
    return com_rasp, braco_dobot

# Faz com que o braço vá até a bandeja, abeixe sua ponta de amostragem, varra a bandeja n vezes e suba novamente
def percorre_bandeja(x0, y0, z0, braco_dobot, x_bandeja, y_bandeja, deslocamento_x_bandeja, deslocamento_y_bandeja, altura_subida, altura_bandeja, n_varreduras, com_eletroima, estado_eletroima):

    # Ir até a bandeja de amostragem
    braco_dobot.move_to(x0 + x_bandeja,
                        y0 + y_bandeja,
                        z0 + altura_subida, 0,
                        wait=True)

    # Controla eletroíma
    controle_eletroima(com_eletroima, estado_eletroima)

    # Descer até a amostra
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + altura_bandeja, 0,
                        wait=True)

    # Percorre bandeja n vezes
    for i in range(n_varreduras):
        braco_dobot.move_to(x0 + x_bandeja + deslocamento_x_bandeja, 
                            y0 + y_bandeja + deslocamento_y_bandeja,
                            z0 + altura_bandeja, 0,
                            wait=True)
   
        braco_dobot.move_to(x0 + x_bandeja,
                            y0 + y_bandeja,
                            z0 + altura_bandeja, 0,
                            wait=True)
          
        print("Varredura ", i, " de ", n_varreduras)

    # Suspender braço acima da bandeja para ir para a próxima
    braco_dobot.move_to(x0 + x_bandeja,
                        y0 + y_bandeja,
                        z0 + altura_subida, 0,
                        wait=True)
    
    return None
    
# Prepara o braço robótico e o eletroíma para o ensaio
def despertar(taxa_transmissao, tempo_espera, altura_subida):
    print("\nConectando com dispositivos...")
    com_dispositivo, braco_robotico = setup(taxa_transmissao,  tempo_espera)
    controle_eletroima(com_dispositivo, "e,0,100,off")
    print("\nZerando braço robótico...")
    (x0, y0, z0, r0, j1, j2, j3, j4) = braco_robotico.pose() 
    print("\nAtivação inicial")
    braco_robotico.move_to(x0, y0, z0 + altura_subida, r0, wait=True)
    print("\nAtivação do eletroíma")
    controle_eletroima(com_dispositivo, "alarme,1")
    controle_eletroima(com_dispositivo, "e,1,100,g")

    return braco_robotico, x0, y0, z0, com_dispositivo

# Desliga o braço robótico e o eletroíma
def adormecer(braco_robotico, com_dispositivo, x0, y0, z0, altura_subida):
    # Retorna o braço para a posição inicial
    braco_robotico.move_to(x0, y0, z0 + altura_subida, 0, wait = True)  
    braco_robotico.move_to(x0, y0, z0, 0, wait = True) 
    controle_eletroima(com_dispositivo, "e,0,100,off")
    braco_robotico.close()
    com_dispositivo.close()

    return None

if __name__ == "__main__":

    # Inicializa o ensaio
    maganalyzer, x0, y0, z0, com_eletroima = despertar(TAXA_TRANSMISSAO_COMUNICACAO, TEMPO_ESPERA_CONEXAO, Poses.ALTURA_SUBIDA.value)

    lista_deflexoes = []
    lista_diferencas = []
    # Executa o ensaio
    for i in range(Ensaio.NUMERO_CICLOS_ENSAIO.value):

        print("\nCiclo ", i, " de ", Ensaio.NUMERO_CICLOS_ENSAIO.value, "\n")

        # Amostra material
        print("Varrendo bandeja de amostragem... \n")
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
        print("\nLavando amostra... \n")
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
        print("\nDepositando amostra... \n")
        percorre_bandeja(x0, y0, z0, 
                        maganalyzer, 
                        Poses.X_BANDEJA_C.value,
                        Poses.Y_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_C.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        50, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        com_eletroima, 
                        AcoesEletroima.DESLIGAR.value)
        
        valor_balanca = int(le_balanca(com_eletroima))
        lista_deflexoes.append(valor_balanca)
        print("\nDeflexão ", i+1, ": ", valor_balanca)

        if len(lista_deflexoes) > 1:
            diferenca = lista_deflexoes[-1] - lista_deflexoes[-2]
            lista_diferencas.append(diferenca)
            print("Diferença entre a última e a penúltima amostra: ", )

    print(lista_deflexoes)
    print()

    controle_eletroima(com_eletroima, "alarme,5")
    df = pd.DataFrame(lista_deflexoes, columns=["diferencas"])
    df.to_csv("diferencas_amostras.csv", index=False)


    # Finaliza o ensaio
    adormecer(maganalyzer, com_eletroima, x0, y0, z0, Poses.ALTURA_SUBIDA.value)