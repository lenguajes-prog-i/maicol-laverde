import pickle

def crear_auto(modelo, placa):
    return {"modelo": modelo, "placa": placa}
 
def representar_auto(auto):
    return f"El auto {auto['modelo']} tiene placa {auto['placa']}"

autos = [

crear_auto("BMW", "ABC123"),

crear_auto("toyota", "CM123"),

crear_auto("Ferrari", "BLB123"),

crear_auto ("mercedes benz", "ELM121"),

crear_auto("Lamborghini veneno", "REA987")

]

with open("autos.txt", "wb") as archivo:
    pickle.dump(autos, archivo)

#Leer archivo

with open("autos.txt", "rb") as archivo:
    autos_cargados = pickle.load(archivo)


list(map(lambda auto: print(representar_auto(auto)), autos_cargados))