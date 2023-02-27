class TV:
    _canal = 1
    _volumen = 1
    _precio  = 500
    _numTV = 0
    
    def __init__(self,marca, canal, precio, estado, volumen, control):
        self.marca = marca
        self._canal = canal
        self._precio = precio
        self._estado = estado
        self._volumen = volumen
        self.control = control
        _numTV += 1

    def setMarca(self, marca):
        self._marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control
    
    def getControl(self):
        return self._control
    
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen
    
    def setCanl(self, canal):
        self._canal = canal

    def getCanal(self):
        return self._canal
    
    def setNumTV(self, numTV): #
        TV.numTV = numTV

    def getNumTV(): #
        return TV.numTV
    
    def getEstado(self):
        return self._estado
    
    def turnOn(self): # Encendido
        self.estado = True

    def turnOff(self): # Apagado
        self.estado = False

    def canalUp(self):
        if bool(self.estado) == True:
            if (self.canal >= 1) and (self.canal < 120):
                self.canal += 1

    def canalDown(self):
        if bool(self.estado) == True:
            if (self.canal > 1) and (self.canal <= 120):
                self.canal -= 1

    def volumenUp(self):
        if bool(self.estado) == True:
            if (self._volumen >= 0) and (self._volumen < 7):
                self._volumen += 1
        

    def volumenDown(self):
        if bool(self.estado) == True:
            if (self._volumen > 0) and (self._volumen <= 7):
                self._volumen -= 1
