from concurrent.futures import thread
import threading
import time
from Personas import *

Inicio_clase = {
    1: [
        "Pepe",
        20,
        "Cuerda"
    ],
    2:[
        "Jose",
        19,
        "Rueda"
    ],
    3: [
        "Angela",
        24,
        "Cuerda"
    ],
    4: [
        "Carlota",
        19,
        "Comba"
    ],
    5: [
        "David",
        23,
        "Comba"
    ],
    6: [
        "Tonacho",
        53,
        "Pesas"
    ]
}

ejercicios = {
    "Cuerda": 2,
    "Rueda": 1,
    "Saltos": 4,
    "Comba": 2,
    "Pesas": 3
}

lista_ejercicios = list(ejercicios.keys())

def realizar_ejercicio(persona):
    ejer = persona.aparato
    print(persona.nombre, "Empieza a hacer", ejer, "a la hora", time.time())
    repeticiones = ejercicios[ejer]
    for i in range(repeticiones):
        print(persona.nombre, "acaba", i + 1, "de", repeticiones, "repeticiones")
    
    print(persona.nombre, "ha acabado con el ejercicio de", ejer, "a la hora", time.time())
    if lista_ejercicios.index(ejer) == 4:
        persona.aparato = lista_ejercicios[0]
    else:
        persona.aparato = lista_ejercicios[lista_ejercicios.index(persona.aparato) + 1]
    

def dirigir_clase(lista_alumnos):
    actividades = []
    for alumno in lista_alumnos:
        x = threading.Thread(target=realizar_ejercicio, args=(alumno,))
        actividades.append(x)
        x.start()



#De aqui pa bajo codigo de ejecutar y tal, no funciones ni nada

Personas_en_clase = setUp_integrantes(Inicio_clase)

dirigir_clase(Personas_en_clase)
