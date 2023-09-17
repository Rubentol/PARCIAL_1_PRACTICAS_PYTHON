#Capitulo 37: Clases y objetos

class Naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuertas = False
    sistemas = True
    autodestruccion = False
    
    def encender(self):
        self.activada = True

    def apagar(self):
        self.activada = False

    def abrir_compuertas(self):
        self.compuertas = True

    def cerrar_compuertas(self):
        self.compuertas = False

    def desactivar_defensas(self):
        self.sistemas = False

    def activar_defensas(self):
        self.sistemas = True

    def activar_autodes(self):
        self.autodestruccion = True

    def estado_motores(self):
        if (self.activada):
            return "Motores trabajando al 100%"
        else:
            return "Motores apagados."
        
    def estado_compuertas(self):
        if(self.compuertas):
            return "La compuerta esta abierta."
        else: 
            return "La compuerta esta cerrada"
        
    def estado_defensa(self):
        if(self.sistemas):
            return "El sistema de defensa esta activado."
        else:
            return "¡PELIGRO! El sistema de defensa esta desactivado."
        
nave1 = Naves()

nave1.encender()
print(nave1.estado_motores())

nave1.apagar()
print(nave1.estado_motores())

nave1.abrir_compuertas()
print(nave1.estado_compuertas())

nave1.cerrar_compuertas()
print(nave1.estado_compuertas())

print(nave1.estado_defensa())
nave1.desactivar_defensas()
print(nave1.estado_defensa())

nave1.activar_autodes()