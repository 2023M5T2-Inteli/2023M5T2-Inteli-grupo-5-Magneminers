from machine import Pin, PWM, UART
from time import sleep
from hx711 import HX711 # - https://github.com/SergeyPiskunov/micropython-hx711
import sys

buzzer = PWM(Pin(22))

ENA = PWM(Pin(11))
In1 = Pin(12, Pin.OUT)
In2 = Pin(13, Pin.OUT)

led_r = Pin(10, Pin.OUT)
led_g = Pin(9, Pin.OUT)

balanca_invertida = HX711(2, 3)

def celula_carga(objeto_carga):
    valor_carga = objeto_carga.read()
    
    return valor_carga

def alarme(pino_buzzer, tom, quantidade, pausa):
    for i in range(quantidade):
        pino_buzzer.duty_u16(33000)
        pino_buzzer.freq(tom)
        sleep(pausa)
        buzzer.duty_u16(0)
        sleep(pausa)
    
    return None

def mapear(x, in_min, in_max, out_min, out_max):
    valor_dimensionado = int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    return valor_dimensionado

def eletroima(pino_eletroima, estado, potencia):
    potencia_rasp = mapear(potencia, 0, 100, 0, 65000)
    if (estado == 1):
        ENA.duty_u16(potencia_rasp)
        In1.value(1)
        In2.value(0)
    elif (estado == 0):
        ENA.duty_u16(potencia_rasp)
        In1.value(0)
        In2.value(1)
        ENA.duty_u16(0)
        
    return None

def luz_indicadora(cor):
    if (cor == "r"):
        led_r.value(1)
        led_g.value(0)
    elif (cor == "g"):
        led_r.value(0)
        led_g.value(1)
    elif (cor == "off"):
        led_r.value(0)
        led_g.value(0)
        
    return None

def envia_serial(mensagem):
    string_mensagem = (str(mensagem) + "\n").encode()
    sys.stdout.write(string_mensagem)
    
    return None

def recebe_serial():
    input_recebido = sys.stdin.readline().strip()
    
    return input_recebido

def testa_firmware(n_ciclos):

    for i in range(n_ciclos):
        alarme(buzzer, 150, 1, 0.5)
        eletroima(ENA, 1, 100)
        luz_indicadora("g")
        sleep(1)

        alarme(buzzer, 300, 1, 0.5)
        eletroima(ENA, 0, 100)
        luz_indicadora("r")
        sleep(1)

        valor = celula_carga(balanca_invertida)
        print(valor)
    
    return None

if __name__ == "__main__":
    
    testa_firmware(0)
    
    while True:
        
        mensagem = recebe_serial().split(",")
        
        if (len(mensagem) > 0):
            
            if (mensagem[0] == "e"):
                eletroima(ENA, int(mensagem[1]), int(mensagem[2]))
                luz_indicadora(mensagem[3])
                
            elif (mensagem[0] == "b"):
                valor = celula_carga(balanca_invertida)
                envia_serial(valor)
                
                
            elif (mensagem[0] == "t"):
                testa_firmware(int(mensagem[1]))
                
            elif(mensagem[0] == "alarme"):
                alarme(buzzer, 550, int(mensagem[1]), 0.5)
                
                
        
