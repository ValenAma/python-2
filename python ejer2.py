# valentina amaya 
# inicializamos la clase
class alumno:
    # inicializamos los atributos
    def __init__(self):
        self.nombre=input("ingresa el nombre del alumno: ")
        self.nota=int(input("ingresa la nota del alumno:  "))

    def mostrar(self):
        print("nombre: ", self.nombre)
        print("nota: ", self.nota)

               
class nota(alumno):
     def _init_(self):
       super()._init_()
       
     def nota_final(self):
       if self.nota >= 3:
          print("la nota del alumno es:", self.nota, "si aprobo")
                 
       else:
          print("la nota del alumno es:", self.nota, "no aprobo")
  
 
 
#bloque principal
nombre=alumno()
nombre.mostrar()
valor=nota()
valor.nota_final()
