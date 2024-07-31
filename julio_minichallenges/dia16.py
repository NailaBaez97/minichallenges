#Formas geométricas: Defina una clase base Forma Geometrica con métodos calcular_area y calcular_perimetro.
#Crea clases derivadas Rectanguloy Circuloque sobrescriben estos métodos.

class Forma_Geometrica():
    def calcular_area(self):
        return None
    def calcular_perimetro(self):
        return None
    
class Rectangulo(Forma_Geometrica):
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
    def calcular_area(self):
        return self.ancho * self.alto
    def calcular_perimetro(self):
        return 2 * (self.ancho +self.alto)
    
class Circulo(Forma_Geometrica):
    PI = 3.141592653589793 
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_perimetro(self):
        return 2 * Circulo.PI * self.radio

rectangulo = Rectangulo(3,4)
circulo = Circulo(5)

print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")