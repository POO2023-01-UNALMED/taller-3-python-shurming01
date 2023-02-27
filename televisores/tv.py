class TV:
    
    _numTV = 0
    
    def __init__(self,marca, estado):
        self.marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self.control = None
        TV._numTV += 1

    def setMarca(self, marca):
        self.marca = marca  
    def getMarca(self):
        return self.marca
    
    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control
    
    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if self.estado == True:
            if (self._volumen >= 0) and (self._volumen <= 7):
                self._volumen = volumen
        
    def getVolumen(self):
        return self._volumen
    
    def setCanal(self, canal):
        if self.estado == True:
            if (self.canal >= 1) and (self.canal < 120):
                self._canal = canal
        
    def getCanal(self):
        return self._canal
    @classmethod
    def setNumTV(cls, cantidad):
        cls.numTV = cantidad
    @classmethod
    def getNumTV(cls): #
        return cls.numTV
    
    def getEstado(self):
        return self._estado

    def turnOn(self): # Encendido
        self.estado = True

    def turnOff(self): # Apagado
        self.estado = False

    def canalUp(self):
        if self.estado == True:
            if (self.canal >= 1) and (self.canal < 120):
                self.canal += 1
    def canalDown(self):
        if self.estado == True:
            if (self.canal > 1) and (self.canal <= 120):
                self.canal -= 1

    def volumenUp(self):
        if self.estado == True:
            if (self._volumen >= 0) and (self._volumen < 7):
                self._volumen += 1
    def volumenDown(self):
        if self.estado == True:
            if (self._volumen >= 0) and (self._volumen <= 7):
                self._volumen -= 1
