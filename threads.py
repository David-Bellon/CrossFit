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

#De aqui pa bajo codigo de ejecutar y tal, no funciones ni nada

Personas_en_clase = setUp_integrantes(Inicio_clase)
