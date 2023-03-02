# Importação das bibliotecas necessárias para o script
import serial 
import serial.tools.list_ports
import pydobot
from time import sleep

TEMPO_ESPERA_CONEXAO = 2 # segundos
TAXA_TRANSMISSAO_COMUNICACAO = 115200 # bits por segundo

# Função para encontrar os COMs disponíveis
def lista_coms():
    coms_encontradas = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in coms_encontradas:
        print(str(item))
    return coms_encontradas

def controle_eletroima(com_serial_ima, estado):
    com_serial_ima.write(str(estado).encode() +b"\n")
    return None

portas_com = lista_coms() # Executa a função escrita a cima

com_eletromima = serial.Serial("COM7", TAXA_TRANSMISSAO_COMUNICACAO, timeout=TEMPO_ESPERA_CONEXAO) # Cria um objeto de comunicação serial

maganalyzer_braco = pydobot.Dobot(port=portas_com[0], verbose=False) # Cria um objeto que controla o braço

(x, y, z, r, j1, j2, j3, j4) = maganalyzer_braco.pose() # Pega a posição atual do braço

print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}') # Imprime a posição atual do braço

# Função para fazer a ponta do braço robótico ir até a bandeja contendo a amostra e percorrer toda sua extensão. Permite que as coordenadas do canto superior esqueda de cada bandeja sejam passadas como parâmetro
def percorre_bandeja(bandeja_canto_x, bandeja_canto_y, com_eletroima):

    maganalyzer_braco.move_to(x + bandeja_canto_x, y - bandeja_canto_y, z + 30, r, wait=True) # Move a ponta do braço para a posição inicial

    controle_eletroima(com_eletroima, 1) # Liga o eletroímã

    # Percorre a bandeja
    print("A")
    maganalyzer_braco.move_to(x + bandeja_canto_x, y - bandeja_canto_y + 30, z + 30, r, wait=True)
    print("B")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10, y - bandeja_canto_y + 30, z + 30, r, wait=True)
    print("C")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10, y - bandeja_canto_y - 3, z + 30, r, wait=True)
    print("D")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10, y - bandeja_canto_y - 3, z + 30, r, wait=True)
    print("E")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10, y - bandeja_canto_y - 3 + 30, z + 30, r, wait=True)
    print("F")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30, z + 30, r, wait=True)
    print("G")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10, y - bandeja_canto_y - 3 , z + 30, r, wait=True)
    print("H")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 , z + 30, r, wait=True)
    print("I")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30 , z + 30, r, wait=True)
    print("J")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30 , z + 30, r, wait=True)
    print("K")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30 , z + 30, r, wait=True)
    print("L")
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3, z + 30, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3, z + 30, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30, z + 30, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3 + 30, z + 30, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3, z + 30, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 10 + 10 + 10 + 10 + 10 + 10 + 10, y - bandeja_canto_y - 3, z + 70, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 70, r, wait=True)

    controle_eletroima(com_eletroima, 3) # Ativa o revolvedor de amostra após o percorrimento da primeira bandeja

    # Executa a lavagem na bandeja do meio
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y, z + 70, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 70, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 40, r, wait=True)

    controle_eletroima(com_eletroima, 0) # Desativa o eletroima

    # Deposita a amostra na última bandeja
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x + 70, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 40, r, wait=True)
    maganalyzer_braco.move_to(x + bandeja_canto_x, y + 100, z + 70, r, wait=True)

for i in range(1):

    a = maganalyzer_braco.pose()

    print("x:", a[0], " y:", a[1], " z:", a[2]) 
    sleep(1)

    maganalyzer_braco.move_to(x, y, z + 70, r, wait=True)

    # Realiza o ciclo de amostragem, lavagem e deposição 3 vezes
    for i in range(3):

        maganalyzer_braco.move_to(x + 50, y - 120, z + 70, r, wait=True)

        percorre_bandeja(50, 120)

# Fecha a conexão com o robô
maganalyzer_braco.close()
