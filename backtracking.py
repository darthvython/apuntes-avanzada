# Ejemplo de backtracking.

# Dada una longitud n de str, encuentra todas las posibles combinaciones uniendo A y B.

def backtracking(cadena: list, n: int) -> None:
    
    # La respuesta está completa?
    if len(cadena) == n:
        print("".join(cadena))
        return
    
    # Ver opciones
    for opcion in ["A", "B"]:
        cadena.append(opcion)
        backtracking(cadena, n)
        cadena.pop()
    
cadena = []

backtracking(cadena, 4)