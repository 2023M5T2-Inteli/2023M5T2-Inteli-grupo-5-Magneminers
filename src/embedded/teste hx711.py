import machine
from hx711 import HX711 # - https://github.com/SergeyPiskunov/micropython-hx711
from time import sleep


# inicializando o modulo HX711 - 
hx = HX711(2, 3)

# Lendo o valor da célula de carga e printando
while True:
    val = hx.read()
    print("Load cell value: ", val)
    sleep(0.1)
    
    