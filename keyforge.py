import itertools
import random

def generar_combinaciones(datos_persona, cantidad):
    combinaciones = set()
    intentos_maximos = 100000
    intentos = 0

    while len(combinaciones) < cantidad and intentos < intentos_maximos:
        num_elementos = random.randint(1, len(datos_persona))
        elementos = random.sample(datos_persona, num_elementos)
        combinacion = ''.join(elementos)
        combinaciones.add(combinacion)
        intentos += 1

    return list(combinaciones)[:cantidad]

def keyforge():
    print("\033[92m" + """
██╗  ██╗███████╗██╗   ██╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
█████╔╝ █████╗   ╚████╔╝ █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██║  ██╗███████╗   ██║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
    """)
    
    print("\033[93m" + "ADVERTENCIA: Esta herramienta está diseñada para ayudar a recordar contraseñas olvidadas.")
    print("El uso malintencionado de esta herramienta es responsabilidad exclusiva del usuario.")
    print("El creador de esta herramienta no se hace responsable de ningún problema derivado de su uso.\n" + "\033[92m")
    
    print("Instrucciones:")
    print("- Cuantos más datos introduzcas, más contraseñas únicas podrás generar.")
    print("- Introduce nombres, apellidos (separados por un espacio), fechas de nacimiento y otros datos relevantes.")
    print("- Separa los 'Otros datos' por comas (ejemplo: mascota, ciudad, afición).\n")
    
    
    datos_1 = []
    nombre_1 = input("Nombre de la persona: ").replace(" ", "")
    
    print("\nIntroduce los apellidos separados por un espacio (ejemplo: Perez Gonzalez):")
    apellidos_1 = input("Apellidos: ").split()
    apellidos_1 = [apellido.replace(" ", "") for apellido in apellidos_1]
    
    while True:
        fecha_nacimiento_1 = input("Fecha de nacimiento (YYYYMMDD): ").replace(" ", "")
        if len(fecha_nacimiento_1) == 8 and fecha_nacimiento_1.isdigit():
            break
        else:
            print("Error: La fecha debe tener exactamente 8 dígitos (YYYYMMDD). Inténtalo de nuevo.\n")
    
    año = fecha_nacimiento_1[:4]
    mes = fecha_nacimiento_1[4:6]
    dia = fecha_nacimiento_1[6:]
    
    print("\nIntroduce otros datos separados por comas (por ejemplo: mascota, ciudad, afición):")
    otros_datos_1 = [dato.replace(" ", "") for dato in input("Otros datos: ").split(',') if dato.strip()]
    
    datos_1.extend([nombre_1] + apellidos_1 + [año, mes, dia] + otros_datos_1)
    
    total_combinaciones = 0
    for i in range(1, len(datos_1) + 1):
        total_combinaciones += len(list(itertools.permutations(datos_1, i)))
    
    print(f"\nCon los datos ingresados, se pueden generar hasta {total_combinaciones} combinaciones únicas.")
    
    while True:
        generar = input("¿Deseas generar las contraseñas? (y/n): ").strip().lower()
        if generar in ['y', 'n']:
            break
        else:
            print("Error: Debes ingresar 'y' para sí o 'n' para no. Inténtalo de nuevo.\n")
    
    if generar != 'y':
        print("Saliendo...")
        return
    
    print("Generando combinaciones...\n")
    
    combinaciones_finales = set()
    combinaciones_finales.update(generar_combinaciones(datos_1, total_combinaciones))
    combinaciones_finales = list(combinaciones_finales)
    random.shuffle(combinaciones_finales)
    
    with open("lista.txt", "w") as archivo:
        for contrasena in combinaciones_finales:
            archivo.write(contrasena + "\n")
    
    print(f"Proceso finalizado. {len(combinaciones_finales)} contraseñas guardadas en lista.txt")
    
    print("Ejemplo de contraseñas generadas:")
    for i, contrasena in enumerate(combinaciones_finales[:10], start=1):
        print(f"{i}. {contrasena}")
    
    print("\033[0m")
    
if __name__ == "__main__":
    keyforge()
