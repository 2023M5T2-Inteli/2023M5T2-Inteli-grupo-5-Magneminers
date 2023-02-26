import sys
from time import sleep
import machine

entrada_sensor_iv = machine.ADC(28)

while True:
    
    leitura_sensor_iv = entrada_sensor_iv.read_u16()
    
    print("Leitura analógica", leitura_sensor_iv)
    sys.stdout.write(leitura_sensor_iv) #Escreve na serial
    sleep(2)