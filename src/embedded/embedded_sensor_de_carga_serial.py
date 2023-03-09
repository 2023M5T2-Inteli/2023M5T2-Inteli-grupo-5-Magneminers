# Importação das bibliotecas e módulos necessários
# Será utilizado o módulo HX711 para a leitura da célula de carga

import machine
import sys
from hx711 import HX711 # - https://github.com/SergeyPiskunov/micropython-hx711
from time import sleep

# Função que lê e retorna os valores da célula de carga

def leitura_sensor_carga(load_cell):
    vlr = load_cell.read()
    return vlr
    
# Função que escreve o valor obtido e envia via serial   

def escrita_serial_sensor_carga(val):
    print("Load cell value: ", val)
    string_mensagem = str(val).encode()
    sys.stdout.write(string_mensagem)
    
    return

# Inicializando o módulo HX711

hx = HX711(2, 3)

# Lendo e exibindo o valor da célula de carga

while True:
    valor = leitura_sensor_carga(hx)
    escrita_serial_sensor_carga(valor)
    sleep(2)
