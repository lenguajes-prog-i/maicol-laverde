import threading


def mostrar_letra(letra):
    for i in range(4):
        print(letra)
    

letras = ["A", "B", "C", "D ", "E", "F", "G", "H", "I", "J", "K", "L","M"]
hilos = []
for letra in letras:
    hilo = threading.Thread(target=mostrar_letra, args=(letra,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()