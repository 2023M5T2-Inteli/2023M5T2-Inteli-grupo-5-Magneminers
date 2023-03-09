# Importação das bibliotecas e módulos necessários
# Será utilizado o módulo HX711 para a leitura da célula de carga

import machine
import sys
from hx711 import HX711 # - https://github.com/SergeyPiskunov/micropython-hx711
from time import sleep


#Função para ler e retornar os valores da célula de carga
def le_valores(load_cell):
    vlr = load_cell.read()
    return vlr
    
#Função para escrever o valor obtido e enviar via serial    
def escreve_serial(val):
    print("Load cell value: ", val)
    string_mensagem = str(val).encode()
    sys.stdout.write(string_mensagem)
    
    return

# inicializando o modulo HX711  
hx = HX711(2, 3)

# Lendo o valor da célula de carga e printando
while True:
    valor = le_valores(hx)
    escreve_serial(valor)
    sleep(2)
