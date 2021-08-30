def calcula_grado(gradoo):
    if gradoo < 0.0 or gradoo > 1.0:
        nota = "score incorrecto"
    elif gradoo > 0.9:
        nota = "A"
    elif gradoo > 0.8:
        nota = "B"
    elif gradoo > 0.7:
        nota = "C"
    elif gradoo > 0.6:
        nota = "D"
    else:
        nota = "F"
    return nota


def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
