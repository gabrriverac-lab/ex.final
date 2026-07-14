peliculas = {
    'P101': ['luz de otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neon', 'accion', 125, 'C', 'Ingles', True],
    'P103': ['Planeta agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Codigo Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficcion', 132, 'b', 'Ingles', False]  
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 25],
    'P105': [8990, 8],
    'P106': [7490, 3]
}

def leer_opcion():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        try:
            opcion = int(input("Ingrese opcion: "))
            if 1 <= opcion  <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True

def validar_clasificacion(clasif):
    if clasif.strip().upper() in ['A', 'B', 'C']:
            return True 
    return False

def validar_duracion(duracion):
    if duracion > 0:
        return True
    return False

def validar_es_3d(respuesta):
    if respuesta.strip().lower() in ['s', 'n']:
        return True
    return False

def validar_precio(precio):
    if precio > 0:
        return True
    return False

def validar_cupos(cupos):
    if cupos >= 0:
        return True
    return False


def cupos_genero(genero, dicc_peliculas, dicc_cartelera):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for codigo, datos in dicc_peliculas.item():
        genero_pelicula = datos[1].strip().lower()
        if genero_pelicula == genero_buscado:
            total_cupos += dicc_cartelera[codigo][1]
    print(f"El total de cupos dosponibles es: {total_cupos}")
    
def busqueda_precio(p_min, p_max, dicc_peliculas, dicc_cartelera):
    preliculas_encotradas = []
    for codigo, datos in dicc_cartelera.items():
        precio = datos[0]
        cupos = datos [1]
        
        if p_min <= precio <= p_max and cupos > 0:
            titulo = dicc_peliculas[codigo][0]
            texto_resultado = f"{titulo}--{codigo}"
            preliculas_encotradas.append(texto_resultado)
            
    if len(preliculas_encotradas) > 0:
        preliculas_encotradas.sort()
        print(f"Las peliculas encontradas son: {preliculas_encotradas}")
    else:
        print("No hay peliculas en ese rango de precios. ")
        
def buscar_codigos(codigo, dicc_peliculas):
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio in dicc_peliculas:
        return False
    return True

def actualizar_precio(codigo, nuevo_precio, dicc_cartelera, dicc_peliculas):
    existe = buscar_codigos(codigo, dicc_peliculas)
    
    if existe:
        codigo_limpio = codigo.strip().upper()
        dicc_cartelera[codigo_limpio][0] = nuevo_precio
        return True
    return False

def agregar_peliculas(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, dicc_peliculas, dicc_cartelera):
    codigo_limpio = codigo.strip().upper()
    
    if buscar_codigos(codigo_limpio, dicc_peliculas):
        return False
    
    es_3d_bool = True if es_3d.strip().lower() == 's' else False
    dicc_peliculas[codigo_limpio] = [titulo, genero, duracion, clasificacion.strip().upper(), idioma, es_3d_bool]
    dicc_cartelera[codigo_limpio] = [precio, cupos]
    
    return True

def eliminar_pelicula(codigo, dicc_peliculas, dicc_cartelera):
    codigo_limpio = codigo.strip().upper()
    if buscar_codigos(codigo_limpio, dicc_peliculas):
        dicc_peliculas.pop(codigo_limpio)
        dicc_cartelera.pop(codigo_limpio)
        return True
    return False




opcion_elegida = 0
while opcion_elegida != 6:
    opcion_elegida = leer_opcion()
    
    if opcion_elegida == 1:
        genero_ingresado = input("Ingrese genero a consultar: ")
        cupos_genero(genero_ingresado, peliculas, cartelera)
        
    elif opcion_elegida == 2:
        while True:
            try:
                p_min = input("Ingrese precio minimo: ")
                p_min = int(p_min)
                p_max = input("Ingrese precio maximo: ")
                p_max = int(p_max)
                
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    busqueda_precio(p_min, p_max, peliculas, cartelera)
                    datos_validos = True
                    
                else:
                    print("El precio minimo debe ser menor o igual al maximo mayores a 0.")
            except ValueError:
                print("Debe ingresar valores enteros")
                
                
    elif opcion_elegida == 3:
        continuar = 's'
        while continuar == 's':
            codigo_ingresado = input("Ingrese codigo de la pelicula: ")
            
            try:
                precio_ingresado = int(input("Ingrese nuevo precio: "))
                if precio_ingresado > 0:
                    resultado = actualizar_precio(codigo_ingresado, precio_ingresado, cartelera, peliculas)
                    if resultado:
                        print("Precio actualizado")
                    else:
                        print("El codigo no existe")
                else:
                    print("El precio debe ser mayor a cero")
            except ValueError:
                print("Error: El precio den+be ser un numero entero.")
                
            continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
    
    
    elif opcion_elegida == 4:
        codigo_n = input("Ingrese codigo de pelicula: ")
        titulo_n = input("Ingrese titulo: ")
        genero_n = input("Ingrese genero: ")
        
        try:
            duracion_n = int(input("Ingrese duración (minutos): "))
        except ValueError:
            duracion_n = -1
            
            clasif_n = input("Ingrese clasificacion: ")
            idioma_n = input("Ingrese idioma: ")
            es_3d_n = input("¿Es 3D? (s/n): ")
            
            try:
                precio_n = int(input("Ingrese precio: "))
            except ValueError:
                precio_n = -1
                
            try:
                cupos_n = int(input("Ingrese cupos:"))
            except ValueError:
                cupos_n = -1
            if not validar_texto(codigo_n):
                print("Error: El código no puede estar vacío.")
            elif not validar_texto(titulo_n):
                print("Error: El título no puede estar vacío.")
            elif not validar_texto(genero_n):
                print("Error: El género no puede estar vacío.")
            elif not validar_duracion(duracion_n):
                print("Error: La duración debe ser un número entero mayor a cero.")
            elif not validar_clasificacion(clasif_n):
                print("Error: La clasificación debe ser exactamente 'A', 'B' o 'C'.")
            elif not validar_texto(idioma_n):
                print("Error: El idioma no puede estar vacío.")
            elif not validar_es_3d(es_3d_n):
                print("Error: Indique 's' o 'n' para 3D.")
            elif not validar_precio(precio_n):
                print("Error: El precio debe ser un número entero mayor a cero.")
            elif not validar_cupos(cupos_n):
                print("Error: Los cupos deben ser un número mayor o igual a cero.")
        else:
           
            exito = agregar_peliculas(codigo_n, titulo_n, genero_n, duracion_n, clasif_n, idioma_n, es_3d_n, precio_n, cupos_n, peliculas, cartelera)
            if exito:
                print("Película agregada")
            else:
                print("El código ya existe")

    elif opcion_elegida == 5:
        codigo_ingresado = input("Ingrese el código de la película a eliminar: ")
        resultado = eliminar_pelicula(codigo_ingresado, peliculas, cartelera)
        
        if resultado:
            print("Película eliminada")
        else:
            print("El código no existe") 
            
    elif opcion_elegida == 6:
        print("Programa finalizado")