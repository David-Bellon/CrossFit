class Persona():
    def __init__(self, nombre, edad, aparato):
        self.nombre = nombre
        self.edad = edad
        self.aparato = aparato
        

def setUp_integrantes(clase):
    personas = []
    todos = list(clase.values())
    for datos_persona in todos:
        persona = Persona(datos_persona[0], datos_persona[1], datos_persona[2])
        personas.append(persona)

    return personas








