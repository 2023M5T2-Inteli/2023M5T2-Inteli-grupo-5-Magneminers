# Importamos as bibliotecas Python que precisamos...
import sys
from machine import Pin

# Definimos os pinos que utilizaremos que estao conectados a Ponte H...
en_a = Pin(0, Pin.OUT) # Pino que liga e desliga a entrada da saida A(esquerda)
in_1 = Pin(1, Pin.OUT) # Pino que determina a polaridade da saida A
in_2 = Pin(2, Pin.OUT) # Pino que determina a polaridade da saida A, esses pinos(in_1 e in_2) dependendo de sua ordem alteram a polaridade da corrente

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

# Testamos se o script esta funcionando corretamente aqui, fazendo com que o eletroima ligue e desligue rapidamente
ligar_eletroima()
sleep(2)

desligar_eletroima()

# Iniciamos o loop do script
while True:
    
    input_recebido = sys.stdin.readline().strip() # Recebemos o Input do Python/usuario
   
   # Dependendo do input recebido do usuario, o eletroima liga ou desliga.
    if input_recebido == "1":
        ligar_eletroima()

    elif input_recebido == "0":
        desligar_eletroima()
       
