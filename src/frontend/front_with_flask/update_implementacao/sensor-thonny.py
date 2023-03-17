# Importação das bibliotecas necessárias
import sys
from time import sleep
import machine

# Definição do pino de entrada analógica do sensor de distância
entrada_sensor_iv = machine.ADC(28)

# Função que realiza a leitura das informações do sensor de distância via serial do Raspberry Pi Pico W
def le_distancia(pino_sensor_iv):
    
   leitura_analogica_sensor_iv = pino_sensor_iv.read_u16() # Leitura da saída analógica do sensor de distância
   leitura_sensor_iv = int(str(leitura_analogica_sensor_iv)[:3]) # Dígitos significativos para o range de distância
   distancia = -4.287e-7*(leitura_sensor_iv**3) + 0.0004954*(leitura_sensor_iv**2) - 0.2097*leitura_sensor_iv + 38.21 # Conversão da saída analógica para unidade de distância
   distancia_ajustada = round(distancia, 2) - 1 # -1 é o offset do suporte do sensor
    
   return distancia_ajustada

# Função que escreve a leitura do sensor de distância no terminal via serial do microcontrolador
def escreve_serial(id_sensor, leitura_numerica):
    
    string_mensagem = (id_sensor + str(leitura_numerica) + "\n").encode()
    sys.stdout.write(string_mensagem)
    
    return string_mensagem

# Loop que realiza a leitura do sensor de distância e a transmissão da informação via serial do microcontrolador
while True:
    
    distancia = le_distancia(entrada_sensor_iv)

    escreve_serial("Distância: ", distancia)
    sleep(0.5)