def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input("Ingresar gasto:\n"))
    print (gasto)
    print("Dinero recibido")
    dinero = int(input("Dinero recibido:\n"))
    print(dinero)
    Vuelto = dinero - gasto
    print("\nVuelto\n")
    pesos= int(Vuelto)
    print ("Pesos:")
    print (pesos)
    centavos = int(round((Vuelto - pesos) * 100))
    print("Centavos:")
    print(centavos)
