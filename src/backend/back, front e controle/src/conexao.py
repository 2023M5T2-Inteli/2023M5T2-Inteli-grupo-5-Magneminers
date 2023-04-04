import serial
import pydobot

#inicia conexão das devidas portas dos aparelhos (dobot e raspberry)

#Raspberry pi pico w
resposta_para_tudo = serial.Serial("COM6", 115200, timeout = 2)

#Dobot
dobot = pydobot.Dobot(port="COM11", verbose=True)