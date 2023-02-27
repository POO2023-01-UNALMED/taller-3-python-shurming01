#from televisores.tv import TV
#from televisores.marca import Marca

class Control:

    def __init__(self):
        self.tv = None

    def turnOn(self): # Encendido
        self.tv.turnOn()

    def turnOff(self): # Apagado
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp() 
        
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.canalDown
       
    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, canal):
        self.tv.setCanal(canal)
    
    def enlazar(self, tv):
        self.tv = tv
        self.control = self

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv



