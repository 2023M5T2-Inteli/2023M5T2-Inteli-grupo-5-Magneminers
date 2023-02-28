import sys
from time import sleep
import machine

def le_distancia(pino_sensor_iv):
    
    leitura_analogica_sensor_iv = pino_sensor_iv.read_u16()
    leitura_sensor_iv = int(str(leitura_analogica_sensor_iv)[:3]) #digitos significativos para nosso range de distância
    distancia = -4.287e-7*(leitura_sensor_iv**3) + 0.0004954*(leitura_sensor_iv**2) - 0.2097*leitura_sensor_iv + 38.21
    distancia_ajustada = round(distancia, 2) - 1 # -1 é o offset do suporte do sensor
    
    return distancia_ajustada

def escreve_serial(id_sensor, leitura_numerica):
    
    string_mensagem = id_sensor + ":" + str(leitura_numerica)
    sys.stdout.write(string_mensagem)
    
    return string_mensagem

entrada_sensor_iv = machine.ADC(28)
    
while True:
    
    distancia = le_distancia(entrada_sensor_iv)
    
    escreve_serial("iv", distancia)
    print("\n")
    sleep(0.5)