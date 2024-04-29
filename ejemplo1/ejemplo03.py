

nombre = str(input('Ingrese nombre de la persona: '))
edad = int(input('Ingrese edad de la persona: '))
sueldo = float(input('Ingrese sueldo de la persona: '))

mensajeFinal = "Nombre: %s\nEdad: %d\nSueldo: %.2f\n"% (
    nombre, edad, sueldo
)
print(mensajeFinal)