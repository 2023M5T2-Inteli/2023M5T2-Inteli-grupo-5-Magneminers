import serial
import pydobot


resposta_para_tudo = serial.Serial("COM7", 115200, timeout = 2)
dobot = pydobot.Dobot(port="COM8", verbose=True)