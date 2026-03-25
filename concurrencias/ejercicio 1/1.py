import threading
import time

print(threading.active_count())
print(threading.enumerate())

def programar():
    print('Inicio 1')
    time.sleep(4)
    print('Finalizo 1')

def beber_agua():
    print('Inicio 2')
    time.sleep(6)
    print('Finalizo 2')

def estudiar():
    print('Inicio 3')
    time.sleep(4)
    print('Finalizo 3')

inicio = time.perf_counter() 

#programar()
#beber_agua()
#estudiar()

hilo_programar = threading.Thread(target=programar, args=())
hilo_programar.start()
hilo_beber_agua = threading.Thread(target=beber_agua, args=())
hilo_beber_agua.start()
hilo_estudiar = threading.Thread(target=estudiar, args=())
hilo_estudiar.start()

hilo_programar.join()
hilo_beber_agua.join()
hilo_estudiar.join()




fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)