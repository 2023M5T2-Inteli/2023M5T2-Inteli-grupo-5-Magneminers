import sys
from time import sleep
from machine import ADC, Pin

# Funcao que faz com que o eletroima seja ligado
def ligar_eletroima():
    en_a.value(1) # Ligamos a entrada de corrente para a saida A
        
    # Aqui fazemos com que a corrente fique positiva para a saida A
    in_1.value(0)
    in_2.value(1) 
    
# Funcao que faz com que o eletroima seja desligado
def desligar_eletroima():
    # Aqui invertemos a polaridade da corrente
    in_1.value(1)
    in_2.value(0)
        
    en_a.value(0) # Desligamos a entrada de corrente para a saida A

def le_distancia(pino_sensor_iv):
    
    leitura_analogica_sensor_iv = pino_sensor_iv.read_u16()
    leitura_sensor_iv = int(str(leitura_analogica_sensor_iv)[:3]) #digitos significativos para nosso range de distância
    distancia = -4.287e-7*(leitura_sensor_iv**3) + 0.0004954*(leitura_sensor_iv**2) - 0.2097*leitura_sensor_iv + 38.21
    distancia_ajustada = round(distancia, 2) - 1 # -1 é o offset do suporte do sensor
    
    return distancia_ajustada

def escreve_serial(id_sensor, leitura_numerica):
    
    string_mensagem = (id_sensor + ":" + str(leitura_numerica) + "\n").encode()
    sys.stdout.write(string_mensagem)
    print()
    
    return string_mensagem

# Definimos os pinos que utilizaremos que estao conectados a Ponte H...
en_a = Pin(0, Pin.OUT) # Pino que liga e desliga a entrada da saida A(esquerda)
in_1 = Pin(1, Pin.OUT) # Pino que determina a polaridade da saida A
in_2 = Pin(2, Pin.OUT) # Pino que determina a polaridade da saida A, esses pinos(in_1 e in_2) dependendo de sua ordem alteram a polaridade da corrente

# Definimos os pinos que utilizaremos para o Infravermelho...
entrada_sensor_iv = ADC(28)

# Testamos se o script esta funcionando corretamente aqui, fazendo com que o eletroima ligue e desligue rapidamente
ligar_eletroima()
sleep(2)
desligar_eletroima()

# Funcionando, prosseguimos para deixa-los em loop.
while True:
    
    input_recebido = sys.stdin.readline().strip()# Recebemos o Input do Python/usuario
    input_recebido_array = input_recebido.split(",")
    
    
    if input_recebido_array[0] == "iv":
        distancia = le_distancia(entrada_sensor_iv)
        print(distancia)
        escreve_serial("iv", distancia)
        sleep(1)
        
    elif input_recebido_array[0] == "ec":
        input_estado_eletroima = input_recebido_array[1]
        # Dependendo do input recebido do usuario, o eletroima liga ou desliga.
        if input_estado_eletroima == "1":
            ligar_eletroima()

        elif input_estado_eletroima == "0":
            desligar_eletroima()