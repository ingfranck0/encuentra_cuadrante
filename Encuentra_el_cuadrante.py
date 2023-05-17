#declarando una def yconfigurando parametros de cuadrante 
def obtener_cuadrante(x, y):
    if x > 0 and y > 0:
        return "Primer cuadrante"
    elif x < 0 and y > 0:
        return "Segundo cuadrante"
    elif x < 0 and y < 0:
        return "Tercer cuadrante"
    elif x > 0 and y < 0:
        return "Cuarto cuadrante"
    else:
        return "El punto está sobre uno de los ejes"
#definicion de las variables 
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

#retornamos lo obtenido
cuadrante = obtener_cuadrante(x, y)
print(f"El punto ({x}, {y}) se encuentra en {cuadrante}")