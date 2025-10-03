# ==============================
#   GESTOR DE NOTAS ACADÉMICAS
# ==============================

# Listas principales
cursos = []
historial = []       # Pila (último en entrar, primero en salir)
cola_revision = []   # Cola (primero en entrar, primero en salir)

def imprimir_menu():
    print("==============================")
    print("  GESTOR DE NOTAS ACADÉMICAS  ")
    print("==============================")
    print(" 1. Registrar nuevo curso")
    print(" 2. Mostrar todos los cursos y notas")
    print(" 3. Calcular promedio general")
    print(" 4. Contar cursos aprobados y reprobados")
    print(" 5. Buscar curso por nombre")
    print(" 6. Actualizar nota de un curso")
    print(" 7. Eliminar un curso")
    print(" 8. Ordenar cursos por nota (Burbuja)")
    print(" 9. Ordenar cursos por nombre (Inserción)")
    print("10. Agregar curso a revisión (Cola)")
    print("11. Atender revisión")
    print("12. Mostrar historial de acciones (Pila)")
    print("13. Salir")

def leer_opcion():
    entrada = input("Seleccione una opción (1-13): ")
    try:
        opcion = int(entrada)
        if opcion in range(1, 14):
            return opcion
        return -1
    except ValueError:
        return -1

# -------------------------------
#   FUNCIONES PRINCIPALES
# -------------------------------

def registrar_curso():
    print("\n--- REGISTRAR NUEVO CURSO ---")
    
    codigo = input("Código del curso: ")
    nombre = input("Nombre del curso: ")
    
    try:
        nota = float(input("Nota del curso (0-100): "))
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100")
            return
    except ValueError:
        print("Error: Ingrese un número válido para la nota")
        return
    
    try:
        creditos = int(input("Créditos del curso (1-10): "))
        if creditos < 1 or creditos > 10:
            print("Error: Los créditos deben estar entre 1 y 10")
            return
    except ValueError:
        print("Error: Ingrese un número válido para los créditos")
        return
    
    curso = {
        "codigo": codigo,
        "nombre": nombre,
        "nota": nota,
        "creditos": creditos
    }
    
    cursos.append(curso)
    historial.append(f"Registrado curso: {nombre}")
    print("Curso registrado exitosamente")

def mostrar_cursos():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    print("\n--- CURSOS REGISTRADOS ---")
    print(f"{'Código':<10} {'Nombre':<25} {'Nota':<8} {'Créditos':<10}")
    print("-" * 55)
    
    for curso in cursos:
        print(f"{curso['codigo']:<10} {curso['nombre']:<25} {curso['nota']:<8} {curso['creditos']:<10}")

def calcular_promedio():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    suma_ponderada = 0
    total_creditos = 0
    
    for curso in cursos:
        suma_ponderada += curso['nota'] * curso['creditos']
        total_creditos += curso['creditos']
    
    promedio = suma_ponderada / total_creditos
    print(f"Promedio ponderado: {promedio:.2f}")

def contar_aprobados_reprobados():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    aprobados = sum(1 for curso in cursos if curso['nota'] >= 61)
    reprobados = len(cursos) - aprobados
    
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_por_nombre():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    nombre_buscar = input("Ingrese el nombre del curso a buscar: ")
    encontrado = False
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"\nCurso encontrado en posición {i}:")
            print(f"Código: {cursos[i]['codigo']}")
            print(f"Nombre: {cursos[i]['nombre']}")
            print(f"Nota: {cursos[i]['nota']}")
            print(f"Créditos: {cursos[i]['creditos']}")
            encontrado = True
            break
    
    if not encontrado:
        print("Curso no encontrado")

def actualizar_nota():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    nombre_buscar = input("Ingrese el nombre del curso a actualizar: ")
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"Curso encontrado: {cursos[i]['nombre']}")
            print(f"Nota actual: {cursos[i]['nota']}")
            
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("Error: La nota debe estar entre 0 y 100")
                    return
                
                cursos[i]['nota'] = nueva_nota
                historial.append(f"Actualizada nota del curso: {cursos[i]['nombre']}")
                print("Nota actualizada exitosamente")
                return
            except ValueError:
                print("Error: Ingrese un número válido")
                return
    
    print("Curso no encontrado")

def eliminar_curso():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    nombre_buscar = input("Ingrese el nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            historial.append(f"Eliminado curso: {cursos[i]['nombre']}")
            del cursos[i]
            print("Curso eliminado exitosamente")
            return
    print("Curso no encontrado")

# -------------------------------
#   ORDENAMIENTOS
# -------------------------------

def ordenar_burbuja():
    n = len(cursos)
    if n == 0:
        print("No hay cursos registrados")
        return
    
    for i in range(n-1):
        for j in range(n-i-1):
            if cursos[j]['nota'] > cursos[j+1]['nota']:
                cursos[j], cursos[j+1] = cursos[j+1], cursos[j]
    print("Cursos ordenados por nota (Burbuja)")

def ordenar_insercion():
    n = len(cursos)
    if n == 0:
        print("No hay cursos registrados")
        return
    
    for i in range(1, n):
        key = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]['nombre'].lower() > key['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
    print("Cursos ordenados por nombre (Inserción)")

# -------------------------------
#   COLA (Revisión)
# -------------------------------

def agregar_revision():
    if len(cursos) == 0:
        print("No hay cursos registrados")
        return
    
    nombre = input("Ingrese el nombre del curso a enviar a revisión: ")
    for curso in cursos:
        if curso['nombre'].lower() == nombre.lower():
            cola_revision.append(curso)
            print(f"Curso '{nombre}' agregado a la cola de revisión")
            return
    print("Curso no encontrado")

def atender_revision():
    if len(cola_revision) == 0:
        print("No hay cursos en la cola de revisión")
        return
    
    curso = cola_revision.pop(0)
    print(f"Atendiendo revisión del curso: {curso['nombre']}")

# -------------------------------
#   PILA (Historial)
# -------------------------------

def mostrar_historial():
    if len(historial) == 0:
        print("El historial está vacío")
        return
    
    print("\n--- HISTORIAL DE ACCIONES ---")
    for accion in reversed(historial):
        print(accion)

# -------------------------------
#   PROGRAMA PRINCIPAL
# -------------------------------

def main():
    while True:
        imprimir_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            registrar_curso()
        elif opcion == 2:
            mostrar_cursos()
        elif opcion == 3:
            calcular_promedio()
        elif opcion == 4:
            contar_aprobados_reprobados()
        elif opcion == 5:
            buscar_por_nombre()
        elif opcion == 6:
            actualizar_nota()
        elif opcion == 7:
            eliminar_curso()
        elif opcion == 8:
            ordenar_burbuja()
        elif opcion == 9:
            ordenar_insercion()
        elif opcion == 10:
            agregar_revision()
        elif opcion == 11:
            atender_revision()
        elif opcion == 12:
            mostrar_historial()
        elif opcion == 13:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")

if __name__ == "__main__":
    main()
