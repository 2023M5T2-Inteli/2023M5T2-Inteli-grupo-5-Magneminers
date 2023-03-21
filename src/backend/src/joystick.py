import pydobot
from conexao import dobot

def coordenadas():
    
    (x0, y0, z0, r0, j10, j20, j30, j40) = dobot.pose() 

    dobot.wait(500)

    return x0, y0, z0

def coordenadas_e():
    
    (x0, y0, z0, r0, j10, j20, j30, j40) = dobot.pose() 

    dobot.wait(500)

    return x0, y0