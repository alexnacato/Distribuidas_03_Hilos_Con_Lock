# Ejercicio 3: Hilos con Lock

## Cómo ejecutar con Docker Compose

Necesitas tener Docker y Docker Compose instalados.

1. Clonar el repositorio:

```bash
git clone https://github.com/alexnacato/Distribuidas_03_Hilos_Con_Lock.git
cd Distribuidas_03_Hilos_Con_Lock
```

2. Ejecutar el script:

```bash
docker compose up
```

3. Al terminar, eliminar el contenedor:

```bash
docker compose down
```



## Descripción

Script en Python que usa hilos (`threading.Thread`) con un ejemplo de la vida
diaria: tres personas (Ana, Luis y Carla) intentan comprar al mismo tiempo
**la última entrada** de un concierto.

> [!NOTE]
> **Condición de carrera:** ocurre cuando varios hilos usan el mismo dato
> compartido (aquí, las entradas disponibles) y el resultado depende del orden en
> que se ejecutan. Sin protección, los tres hilos verían "hay 1 entrada" antes de
> que alguno compre, y se venderían más entradas de las que existen.

**Solución:** `threading.Lock()`. Con `with lock`, solo un hilo a la vez puede
consultar y comprar. Ana compra la entrada, y Luis y Carla encuentran que ya
no hay.




> [!IMPORTANT]
> El orden de los nombres puede cambiar entre ejecuciones (por ejemplo, que
> compre Luis primero), porque depende de qué hilo obtiene el lock. El
> resultado final es siempre el mismo: se vende una sola entrada.

## Archivos

- [`03_hilos_lock.py`](03_hilos_lock.py): script en Python.
- [`docker-compose.yml`](docker-compose.yml): configuración para ejecutarlo con Docker Compose
  (usa la imagen `python:3.11-alpine`).
- [`README.md`](README.md): este archivo.