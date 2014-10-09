

class Animal():

    def __init__(self,**args):
        self.nombreCientifico = args["nombreCientifico"] if "nombreCientifico" in args else ""

    def setNombreCientifico(self,nombreCientifico):
        self.nombreCientifico = nombreCientifico

    def setNombreComun(self, nombreComun):
        self.nombreComun = nombreComun

    def getNombreCientifico(self):
        return self.nombreCientifico

    def queSoy(self):
        return "Soy un animal"

class Perro(Animal):
  pass

class Gato(Animal):
  pass

class Puerco(Animal):
  pass
