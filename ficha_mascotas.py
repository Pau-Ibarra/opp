class Pet:

    def __init__(self, first_name, last_name, race, age, size):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.size = size
        self.race = race

    def presentacion(self):
        print(f"Mi nombre es {self.first_name} {self.last_name}. Soy un {self.race} de {self.age} años y peso {self.size} kilos.")

gaston = Pet("Gaston Genaro", "Gatuso Aceituno", "gato", "12", "7")
haru = Pet("Haru de las Nieves", "Perez Cotapos Risopatron", "perro", "3", "26")
#el método(función) es dependiente de la clase, por tanto, no puedo llamarlo por si solo. no puedo decir presentación(), debo decir gaston.presentacion()
#el método se llama desde la instancia de una clase (instancia gaston haru)
gaston.presentacion()
haru.presentacion()

    def adelgazar(self,peso_requerido):
        self.size -= peso_requerido
        
gaston.adelgazar()
haru.adelgazar()         
        print (f "Gaston debe bajar {gaston.adelgazar}")
        