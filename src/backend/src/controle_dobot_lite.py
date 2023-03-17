# Importação das bibliotecas necessárias para o script
from enum import Enum
from conexao import resposta_para_tudo, dobot
from main import posicoes, ensaios

global Poses, AcoesEletroima, Ensaio

class AcoesEletroima(Enum):
    LIGAR = 1
    DESLIGAR = 0

# Enumeração das posições do Dobot Magician Lite
class Poses(Enum):

    ALTURA_SUBIDA = 70
    ALTURA_BANDEJA = 30

    X_BANDEJA_A = posicoes[0].x1
    Y_BANDEJA_A = posicoes[0].y1
    DESLOCAMENTO_X_BANDEJA_A = ensaios[0].bd1
    DESLOCAMENTO_Y_BANDEJA_A = ensaios[0].bd2

    X_BANDEJA_B = posicoes[1].x1
    Y_BANDEJA_B = posicoes[1].y1
    DESLOCAMENTO_X_BANDEJA_B = ensaios[0].bd1
    DESLOCAMENTO_Y_BANDEJA_B = ensaios[0].bd2

    X_BANDEJA_C = posicoes[2].x1
    Y_BANDEJA_C = posicoes[2].y1
    DESLOCAMENTO_X_BANDEJA_C = ensaios[0].bd1
    DESLOCAMENTO_Y_BANDEJA_C = ensaios[0].bd2

# Configurações do ensaio
class Ensaio(Enum):
    NUMERO_VARRERUDAS_AMOSTRA = ensaios[0].vrr
    NUMERO_CICLOS_ENSAIO = ensaios[0].cic

# Envia um comando para o Raspberry Pi Pico controlar o eletroímã
def controle_eletroima(com_serial_ima, estado):
        com_serial_ima.write(str(estado).encode() +b"\n")
        return None


# Faz com que o braço vá até a bandeja, abeixe sua ponta de amostragem, varra a bandeja n vezes e suba novamente
def percorre_bandeja(x0, y0, z0, braco_dobot, x_bandeja, y_bandeja, deslocamento_x_bandeja, deslocamento_y_bandeja, altura_subida, altura_bandeja, n_varreduras, com_eletroima, estado_eletroima):

    def controle_eletroima(com_serial_ima, estado):
        com_serial_ima.write(str(estado).encode() +b"\n")
        return None

    # Ir até a bandeja de amostragem
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + altura_subida,
                        0,
                        wait = True)  
    
    # Controla eletroíma
    controle_eletroima(com_eletroima, estado_eletroima)

    # Descer até a amostra
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + Poses.ALTURA_BANDEJA.value,
                        0,
                        wait = True)  
    
    # Percorre bandeja n vezes
    for i in range(n_varreduras):
        braco_dobot.move_to(x0 + x_bandeja + deslocamento_x_bandeja, 
                            y0 + y_bandeja + deslocamento_y_bandeja,
                            z0 + altura_bandeja,
                            0,
                            wait = True) 
        
        braco_dobot.move_to(x0 + x_bandeja, 
                            y0 + y_bandeja,
                            z0 + altura_bandeja,
                            0,
                            wait = True)  
        
        print("Varredura ", i, " de ", n_varreduras)

    # Suspender braço acima da bandeja para ir para a próxima
    braco_dobot.move_to(x0 + x_bandeja, 
                        y0 + y_bandeja,
                        z0 + altura_subida,
                        0,
                        wait = True)  
    
    return None
    
# Prepara o braço robótico e o eletroíma para o ensaio
def despertar(dobot, altura_subida):
    
    (x0, y0, z0, r0, j10, j20, j30, j40) = dobot.pose() 
    dobot.move_to(x0, y0, z0 + altura_subida, r0, wait=True)

    return x0, y0, z0, r0

# Desliga o braço robótico e o eletroíma
def adormecer(braco_robotico, com_dispositivo, x0, y0, z0, r0, altura_subida):
    # Retorna o braço para a posição inicial
    braco_robotico.move_to(x0, y0, z0 + altura_subida, r0, wait = True)  
    braco_robotico.move_to(x0, y0, z0, r0, wait = True) 
    
    braco_robotico.close()
    com_dispositivo.close()

    return None

if __name__ == "__main__":

    x0, y0, z0, r0 = despertar(dobot, Poses.ALTURA_SUBIDA.value)

    for i in range(Ensaio.NUMERO_CICLOS_ENSAIO.value):

        # Amostra material
        percorre_bandeja(x0, y0, z0, 
                        dobot, 
                        Poses.X_BANDEJA_A.value,
                        Poses.Y_BANDEJA_A.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_A.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_A.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        resposta_para_tudo, 
                        AcoesEletroima.LIGAR.value)

        # Lava material
        percorre_bandeja(x0, y0, z0, 
                        dobot, 
                        Poses.X_BANDEJA_B.value,
                        Poses.Y_BANDEJA_B.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_B.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_B.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        resposta_para_tudo, 
                        AcoesEletroima.LIGAR.value)

        # Deposita material
        percorre_bandeja(x0, y0, z0, 
                        dobot, 
                        Poses.X_BANDEJA_C.value,
                        Poses.Y_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_X_BANDEJA_C.value, 
                        Poses.DESLOCAMENTO_Y_BANDEJA_C.value, 
                        Poses.ALTURA_SUBIDA.value, 
                        Poses.ALTURA_BANDEJA.value, 
                        Ensaio.NUMERO_VARRERUDAS_AMOSTRA.value, 
                        resposta_para_tudo, 
                        AcoesEletroima.DESLIGAR.value)
        
    # Finaliza o ensaio
    adormecer(dobot, resposta_para_tudo, x0, y0, z0, r0, Poses.ALTURA_SUBIDA.value)