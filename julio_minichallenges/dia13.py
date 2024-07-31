#Cuenta bancaria: Implementa una clase CuentaBancariacon métodos para depositar y consultar el saldo.
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depositados gs{cantidad}. Saldo actual: gs{self.saldo}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retirados gs{cantidad}. Saldo actual: gs{self.saldo}.")
        else:
            print("Fondos insuficientes o cantidad invalida.")

    def consultar_saldo(self):
        print(f"Saldo actual: gs{self.saldo}.")
        return self.saldo

    def menu(self):
        while True:
            selec = input("Escoge una accion: DEPOSITAR 'D', RETIRAR 'R', SALIR 'S', para ver informacion 'I': ").upper()
            if selec == 'D':
                cantidad = float(input("Ingresa el monto a depositar: "))
                self.depositar(cantidad)
            elif selec == 'R':
                cantidad = float(input("Ingresa el monto a retirar: "))
                self.retirar(cantidad)
            elif selec == 'I':
                self.consultar_saldo()
            elif selec == 'S':
                print("Gracias por usar el servicio bancario.")
                break
            else:
                print("Opcion no valida, por favor intenta de nuevo.")

# Ejemplo de uso
if __name__ == '__main__':
    cuenta = CuentaBancaria(0) 
    cuenta.menu()  
