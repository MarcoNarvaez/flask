#funcion lambda

lista = [1,2,3,4,5,6]

filtro = filter(lambda numero: (numero % 2) == 0, lista)
pares = list(filtro)
print(pares)

#POO

class Persona():
    def __init__(self,nombre):
        self.nombre = nombre
    def saludar(self):
        self.texto = "Hola, mi nombre es " + self.nombre
        return self.texto
        
persona1 = Persona('Marco')
print(type(persona1))
print(persona1.nombre)
texto = persona1.saludar()
print(texto)

class Adulto(Persona):
    def __init__(self, nombre):
        Persona.__init__(self, nombre)
    def saludar(self):
        self.texto = "hola soy adulto"
        return self.texto
    def grabar_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta
        
adulto1 = Adulto("Marco")
print(type(adulto1))
texto = adulto1.saludar()
print(texto)
adulto1.grabar_tarjeta("1354564")
print(adulto1.tarjeta)