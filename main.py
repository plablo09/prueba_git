from clases.animales import Animal

def main():
  mi_animal = Animal(nombreCientifico="kaninus latosus")

  mi_animal.setNombreComun("mi perro")

  print mi_animal.getNombreCientifico()
  print mi_animal.queSoy()


if __name__ == "__main__":
    main()
