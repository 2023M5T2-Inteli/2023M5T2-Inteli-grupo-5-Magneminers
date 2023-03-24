from machine import Pin, PWM, UART
from time import sleep
from hx711 import HX711 # - https://github.com/SergeyPiskunov/micropython-hx711

buzzer = PWM(Pin(22))

ENA = PWM(Pin(11))
In1 = Pin(12, Pin.OUT)
In2 = Pin(13, Pin.OUT)

a = Pin(10, Pin.OUT)
b = Pin(9, Pin.OUT)

uart = UART(1, baudrate=115200)
uart.init(bits=8, parity=None, stop=2)

hx = HX711(2, 3)

def le_valores(load_cell):
    vlr = load_cell.read()
    return vlr

def alarme(pino_buzzer, tom, quantidade, pausa):
    for i in range(quantidade):
        pino_buzzer.duty_u16(33000)
        pino_buzzer.freq(tom)
        sleep(pausa)
        buzzer.duty_u16(0)
        sleep(pausa)
    
    return None

def mapear(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

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
        a.value(1)
        b.value(0)
    elif (cor == "g"):
        a.value(0)
        b.value(1)
        
    return None

    
if __name__ == "__main__":
    
    while True:
        alarme(buzzer, 150, 1, 0.5)
        eletroima(ENA, 1, 100)
        luz_indicadora("g")
        sleep(1)
        alarme(buzzer, 300, 1, 0.5)
        eletroima(ENA, 0, 100)
        luz_indicadora("r")
        sleep(1)
        valor = le_valores(hx)
        print(valor)




