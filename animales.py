

class Animal():

    def__init__(self,**args):
      self.nombreCientifico = args["nombreCientifico"]if "nombreCientifico" in args else""

    def setNombreCientifico(self,nombreCientifico):
      self.nombreCientifico = nombreCientifico

    def setNombreComun(self, nombreComun):
      self.nombreComun = nombreComun

    def getNombreCientifico(self):
      return self.nombreCientifico

    def quesoy(self):
      return "soy un animal"

  class Perro(Animal):
      pass

class Gato(Animal):
    def __init__(self,nombre,edad,raza):
        self.nombreCientifico ="felix"
        self.nombre = nombre
        self.edad = edad
        self.raza = raza


class Cerdo(Animal):
      pass
