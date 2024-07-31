#Auto y Motor: Implementa una clase Auto que contiene una instancia de una clase Motor con un método para describir
#  el motor.

class Motor():
    def __init__(self,tipo: str):
        self.tipo = tipo
    def describir(self):
        return f"El motor es de tipo {self.tipo}"
class Auto():
    def __init__(self,marca,modelo,motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    def describir_motor(self):
        return self.motor.describir()
motor_v8 = Motor("V8")

mi_auto =Auto("Ford","Mustang",motor_v8)

print(mi_auto.describir_motor())

