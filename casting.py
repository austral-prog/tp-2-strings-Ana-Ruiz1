def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    Precio= int(input("Ingresa el precio: "))
    Descuento= float(input("Ingresa el descuento: "))
    Cantidad = int(input("Ingresa la cantidad: "))
    Precio_descuento= (Precio - ((Precio * Descuento)/ 100)
    Total= Precio_descuento * Cantidad
    print (f"Precio: {Precio}")
    print(f"Descuento: {Descuento}")
    print(f"Precio con descuento: {Precio_descuento}")
    print(f"Total: {Total}")
