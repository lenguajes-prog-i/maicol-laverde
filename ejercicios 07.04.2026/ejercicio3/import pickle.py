import pickle

class auto():
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

        def __repr__(self):
            return f"el auto{self.modelo} tiene placa {self.placa}"
        
        objeto_auto = auto("mazda", "ABC123")
        objeto_auto1 = auto("mercedes", "ABC123")
        objeto_auto2 = auto("ferrari", "ABC123")
        objeto_auto3 = auto("mazda", "ABC123")
        objeto_auto4 = auto("mazda", "ABC123")

        autos = [objeto_auto, objeto_auto1, objeto_auto2, objeto_auto3, objeto_auto4]

        print(objeto_auto)
        print(objeto_auto1)
        print(objeto_auto2)

        archivo_auto = open("mazda.txt", "wb")
        pickle.dump(objeto_auto, archivo_auto)
        archivo_auto.close()

        archivo_auto = open("autos.txt", "wb")
        autos = pickle.load(archivo_auto)
        archivo_auto.close()

        for auto in autos:
        print(auto)


        print(autos)
