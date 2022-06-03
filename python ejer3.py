# valentina amaya 
class Calculadora:
	def __init__(self):
		self.numero1=int(input("Ingrese el primer numero: "))
		self.numero2=int(input("Ingrese el segundo numero: "))
 
	def suma(self):
		suma=self.numero1+self.numero2
		print("El resultado de la suma de los numeros es: ",suma)
 
	# función para restar
	def resta(self):
		resta=self.numero1-self.numero2
		print("El resultado de la resta de los numeros es: ",resta)
 
	# función para calcular el producto
	def multiplicacion(self):
		pro=self.numero1*self.numero2
		print("El resultado de la multiplicación de los numeros es: ",pro)
 
	# función para dividir
	def division(self):
		div=self.numero1/self.numero2
		print("El resultado de la división de los numeros es: ",div)
 
	# función para imprimir
	def imprimir(self):
		print("Los numero son: ")
		print("numero 1: ",self.numero1)
		print("numero 2: ",self.numero2)
 
 
# bloque principal
calcular=Calculadora()
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()
