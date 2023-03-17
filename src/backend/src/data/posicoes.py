class Posicao():
    def __init__(self, x1, y1, z1) -> None:
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.z1 = int(z1)
        # self.xd1 = int(xd1)
        # self.yd1 = int(yd1)

        # self.x2 = int(x2)
        # self.y2 = int(y2)
        # self.z2 = int(z2)
        # self.xd2 = int(xd2)
        # self.yd2 = int(yd2)

        # self.x3 = int(x3)
        # self.y3 = int(y3)
        # self.z3 = int(z3)
        # self.xd3 = int(xd3)
        # self.yd3 = int(yd3)

        # self.ptc = int(ptc)
        # self.vrr = int(vrr)
        # self.cic = int(cic)

class Ensaio():
    def __init__(self, bd1, bd2, vrr, cic) -> None:
        self.bd1 = int(bd1)
        self.bd2 = int(bd2)
        self.vrr = int(vrr)
        self.cic = int(cic)