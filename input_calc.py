def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int(input("Ingresa la base:"))
    altura= int(input("Ingresa la altura:"))
    area= base * altura
    perimetro= (2*base) + (2*altura)
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")
