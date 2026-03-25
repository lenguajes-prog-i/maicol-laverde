import threading
import time



def tarea(numero):
    print('Numero de Hilo: ', (numero) )

hilos = []

inicio = time.perf_counter() 

for i in range(1,1000):
    hilo = threading.Thread(target= tarea, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)