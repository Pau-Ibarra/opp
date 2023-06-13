import math
class Cuenta_bancaria:

    cuentas =[] # Aquí se almacenarán todas las instancias de la clase Cuenta_bancaria

    def __init__(self, nombre_cuenta, saldo, tasa_interes = 0.01):
        self.nombre_cuenta = nombre_cuenta
        self.saldo = saldo
        self.tasa_interes = tasa_interes
        Cuenta_bancaria.cuentas.append(self) # Así se agrega la instancia a la lista de cuentas

    def deposito(self, amount):
        self.saldo +=amount
        return self

    def retiro(self, amount):
        if amount<=self.saldo:
            self.saldo -=amount
        else:
            print("Saldo insuficiente: se aplicara un cobro de $5 por concepto de sobregiro.")
            self.saldo -=(amount+5)
        return self

    
    def mostrar_info_cuenta(self):
        print(f"Tu saldo es:  ${math.ceil(self.saldo)}")
        return self

    def generar_interes(self):
        
        if self.saldo >0:
            self.saldo *= (1+ self.tasa_interes)
            print(f"Has ganado ${round(self.saldo * self.tasa_interes, 4)} por concepto de interes.")
        else:
            print("Tu saldo es insuficiente para aplicar ganancia por interes.")
        return self
    
    @classmethod
    def imprimir_info_cuentas(cls):
        for cuenta in cls.cuentas:
            print(f"el saldo de la {cuenta.nombre_cuenta} es ${math.ceil(cuenta.saldo)} y su tasa de interes es del {math.floor(cuenta.tasa_interes*100)}%")

cuenta1 =Cuenta_bancaria("Cuenta 1", 500)
cuenta2 =Cuenta_bancaria("Cuenta 2", 150)
cuenta3 =Cuenta_bancaria("Cuenta 3", 0)

print("------------Saldo cuenta1------------")
cuenta1.deposito(350).deposito(50).deposito(20).retiro(120).generar_interes().mostrar_info_cuenta()
print("------------Saldo cuenta2------------")
cuenta2.deposito(400).deposito(50).retiro(50).retiro(220).retiro(20).retiro(120).generar_interes().mostrar_info_cuenta()
print("------------Saldo cuenta3------------")
cuenta3.deposito(300).deposito(50).retiro(50).retiro(220).retiro(20).retiro(120).generar_interes().mostrar_info_cuenta()
print("------------Todas las instancias de la clase Cuenta_bancaria------------")
Cuenta_bancaria.imprimir_info_cuentas()