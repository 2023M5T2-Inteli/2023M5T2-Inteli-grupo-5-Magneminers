import serial
import pydobot

#inicia conexão das devidas portas dos aparelhos (dobot e raspberry)

#Raspberry pi pico w
resposta_para_tudo = serial.Serial("COM5", 115200, timeout = 2)

#Dobot
dobot = pydobot.Dobot(port="COM8", verbose=True)