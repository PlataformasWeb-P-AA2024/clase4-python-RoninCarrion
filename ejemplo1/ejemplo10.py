"""

"""


archivo = open("ejemplo1/data/atp_tennis.csv", "r")

lineas = archivo.readlines()
print(len(lineas))


lineas = [l.split("|") for l in lineas]
contador = 1
for x in lineas:
    
    cadena = """<b>Torneo:</b> %s<br> <b>Ganador:</b> %s""" % (x[0], x[9])
    print(cadena)
    print(contador)

    archivo_generado = open("ejemplo1/winners_of_tournaments/%s-%s-%s.html" % (x[9], x[0], x[1]), "w")
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close()
    contador+=1