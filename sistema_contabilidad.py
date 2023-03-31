# Importa las bibliotecas necesarias
import csv
import os

# Crea una clase para una transacción
class Transaccion:
    def __init__(self, fecha, concepto, monto, categoria):
        self.fecha = fecha
        self.concepto = concepto
        self.monto = monto
        self.categoria = categoria

# Crea una función para leer el archivo de transacciones
def leer_transacciones(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        siguiente(lector_csv) # Ignora la primera fila
        for fila in lector_csv:
            fecha = fila[0]
            concepto = fila[1]
            monto = float(fila[2])
            categoria = fila[3]
            transaccion = Transaccion(fecha, concepto, monto, categoria)
            transacciones.append(transaccion)
    return transacciones

# Crea una función para agregar una nueva transacción
def agregar_transaccion(nombre_archivo, transaccion):
    with open(nombre_archivo, "a", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([transaccion.fecha, transaccion.concepto, transaccion.monto, transaccion.categoria])

# Crea una función para generar un informe de transacciones
def generar_informe(nombre_archivo, categoria):
    total = 0
    with open(nombre_archivo, "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        siguiente(lector_csv) # Ignora la primera fila
        for fila in lector_csv:
            if fila[3] == categoria:
                total += float(fila[2])
    return total

# Crea una función para eliminar una transacción
def eliminar_transaccion(nombre_archivo, transaccion):
    transacciones = leer_transacciones(nombre_archivo)
    transacciones.remove(transaccion)
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Fecha", "Concepto", "Monto", "Categoría"])
        for transaccion in transacciones:
            escritor_csv.writerow([transaccion.fecha, transaccion.concepto, transaccion.monto, transaccion.categoria])

# Crea una función para editar una transacción
def editar_transaccion(nombre_archivo, transaccion_original, transaccion_nueva):
    transacciones = leer_transacciones(nombre_archivo)
    indice = transacciones.index(transaccion_original)
    transacciones[indice] = transaccion_nueva
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Fecha", "Concepto", "Monto", "Categoría"])
        for transaccion in transacciones:
            escritor_csv.writerow([trans
