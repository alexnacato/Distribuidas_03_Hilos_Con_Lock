import threading
import time

# Tres personas intentan comprar la última entrada de un concierto al mismo
# tiempo. Cada persona es un hilo. Sin lock, los tres verían "hay 1 entrada"
# y comprarían (condición de carrera). Con lock, solo uno compra a la vez.

entradas = 2
lock = threading.Lock()


def comprar(nombre):
    global entradas
    with lock:  # Solo un hilo a la vez puede consultar y comprar
        print(f"{nombre} consulta: hay {entradas} entrada(s)")
        if entradas > 0:
            time.sleep(1)  # Simula el procesamiento del pago
            entradas -= 1
            print(f"{nombre} compró una entrada.")
        else:
            print(f"{nombre} no pudo comprar: entradas agotadas.")


hilo1 = threading.Thread(target=comprar, args=("Ana",))
hilo2 = threading.Thread(target=comprar, args=("Luis",))
hilo3 = threading.Thread(target=comprar, args=("Carla",))

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

print(f"\nEntradas disponibles: {entradas}")
