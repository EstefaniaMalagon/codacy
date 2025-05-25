def saludar(nombre): 
    print(f"Hola {nombre}") 
 
def dividir(a, b): 
    if b == 0:
        print("Error: división por cero")
        return None
    return a / b 
 
saludar("Mundo") 
resultado = dividir(10, 0)
if resultado is not None:
    print(resultado)
