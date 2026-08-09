from __future__ import annotations
from typing import List
class Persona:
    def __init__(self, nombre: str, edad : int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.amigos : List[Persona] = []
        
    def saludar(self: Persona, persona : Persona) -> None:
        print(f"{self.nombre}: Hola {persona.nombre}!")
        
fernando = Persona("Fernando",22)
benja = Persona("Benja",23)