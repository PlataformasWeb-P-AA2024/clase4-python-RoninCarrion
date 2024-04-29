"""

"""


archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()
print(len(lineas))


lineas = [l.split("|") for l in lineas]
contador = 0
for x in lineas:
    
    cadena = """<b>Torneo:</b> %s<br> <b>Ganador:</b> %s""" % (x[0], x[9])
    print(cadena)

    archivo_generado = open("data/%s%d.html" % (x[9], contador), "w")
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close()
    contador+=1