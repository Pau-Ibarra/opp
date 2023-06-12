class Usuario:
    def __init__(self, first_name, last_name, saldo):
        self.first_name = first_name
        self.last_name = last_name
        self.saldo = saldo

    def hacer_retiro(self, cantidad):
        self.saldo -= cantidad

    def hacer_deposito(self, cantidad):
        self.saldo += cantidad
        
    def transferir (self,otro_usuario,cantidad): 
        self.hacer_retiro (cantidad)
        otro_usuario.hacer_deposito (cantidad)
        print(f"{self.first_name} {self.last_name} ha transferido ${cantidad} a {otro_usuario.first_name} {otro_usuario.last_name}")

    def mostrar_saldo(self):
        print (f"{self.first_name} {self.last_name} tu saldo es ${self.saldo}")

gaston = Usuario("Gaston Genaro", "Gatuso Aceituno", 850000)
haru = Usuario ("Haru de las Nieves", "Perez Cotapos Risopatron", 2700030)
climbi = Usuario ("Climbi", "Cachirulo", 1500)

gaston.hacer_deposito(50000)
gaston.hacer_deposito(150000)
gaston.hacer_deposito(10000)
gaston.hacer_retiro(100000)
gaston.mostrar_saldo()

print("---------")
haru.hacer_deposito(180000)
haru.hacer_deposito(200000)
haru.hacer_retiro(1000000)
haru.hacer_retiro(3000)
haru.mostrar_saldo()

print("---------")
climbi.hacer_deposito(5000)
climbi.hacer_retiro(1000)
climbi.hacer_retiro(500)
climbi.hacer_retiro(300)
climbi.mostrar_saldo()

print("---------")
#transferencia Gaston a Climbi
gaston.transferir(climbi, 160000)

gaston.mostrar_saldo()
climbi.mostrar_saldo()
