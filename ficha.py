def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    print("=" * 24)
    print("""    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {nombre_limpio[0]}{nombre_limpio[pos_espacio + 1]}")
    print(f"Usuario: {nombre_limpio[pos_espacio + 1:].lower()}.{nombre_limpio[:pos_espacio].lower()}")
    print(f"Email valido: {'@' in email}")
    print(f"Dominio: {email[pos_arroba + 1:].lower()}")
    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")
    print(f"Codigo secreto: {nombre_limpio.upper()[::-1]}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {nota_1 + nota_2 + nota_3}")
    print(f"Promedio: {(nota_1 + nota_2 + nota_3) / 3}")
    print(f"Promedio entero: {(nota_1 + nota_2 + nota_3) // 3}")
    print("=" * 24)
