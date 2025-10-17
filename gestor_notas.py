# GESTOR DE NOTAS ACADEMICAS

# Listas principales
cursos = []
historial = []
cola_revision = []
contador_cursos = 0

# Funciones de validacion

def validar_nota(nota):
    return 0 <= nota <= 100

def validar_creditos(creditos):
    return 1 <= creditos <= 10

def validar_opcion_menu(opcion):
    return 1 <= opcion <= 15

# Funciones de menu

def imprimir_menu():
    print("\n" + "="*50)
    print("        GESTOR DE NOTAS ACADEMICAS")
    print("="*50)
    print(f"  Cursos registrados: {len(cursos)}")
    print(f"  Historial de acciones: {len(historial)}")
    print(f"  Cursos en revision: {len(cola_revision)}")
    print("="*50)
    print(" 1. Registrar nuevo curso")
    print(" 2. Mostrar todos los cursos y notas")
    print(" 3. Calcular promedio general")
    print(" 4. Contar cursos aprobados y reprobados")
    print(" 5. Buscar curso por nombre (Lineal)")
    print(" 6. Buscar curso por codigo (Binaria)")
    print(" 7. Actualizar nota de un curso")
    print(" 8. Eliminar un curso")
    print(" 9. Ordenar cursos por nota (Burbuja)")
    print("10. Ordenar cursos por nombre (Insercion)")
    print("11. Ordenar cursos por codigo (Seleccion)")
    print("12. Agregar curso a revision (Cola)")
    print("13. Atender revision")
    print("14. Mostrar historial de acciones (Pila)")
    print("15. Salir")
    print("="*50)

def leer_opcion():
    entrada = input("Seleccione una opcion (1-15): ")
    try:
        opcion = int(entrada)
        if validar_opcion_menu(opcion):
            return opcion
        return -1
    except ValueError:
        return -1

# Funciones principales

def registrar_curso():
    global contador_cursos
    
    print("\n--- REGISTRAR NUEVO CURSO ---")
    
    codigo = input("Codigo del curso (ej: MAT101): ").strip()
    if not codigo:
        print("Error: El codigo no puede estar vacio")
        return
    
    for curso in cursos:
        if curso['codigo'].lower() == codigo.lower():
            print("Error: Ya existe un curso con ese codigo")
            return
    
    nombre = input("Nombre del curso: ").strip()
    if len(nombre) < 3:
        print("Error: El nombre debe tener al menos 3 caracteres")
        return
    
    try:
        nota = float(input("Nota del curso (0-100): "))
        if not validar_nota(nota):
            print("Error: La nota debe estar entre 0 y 100")
            return
    except ValueError:
        print("Error: Ingrese un numero valido para la nota")
        return
    
    try:
        creditos = int(input("Creditos del curso (1-10): "))
        if not validar_creditos(creditos):
            print("Error: Los creditos deben estar entre 1 y 10")
            return
    except ValueError:
        print("Error: Ingrese un numero valido para los creditos")
        return
    
    contador_cursos += 1
    
    curso = {
        "id": contador_cursos,
        "codigo": codigo.upper(),
        "nombre": nombre,
        "nota": nota,
        "creditos": creditos
    }
    
    cursos.append(curso)
    historial.append(f"Registrado curso: {nombre} ({codigo})")
    print("Curso registrado exitosamente")

def mostrar_cursos():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    print("\n--- CURSOS REGISTRADOS ---")
    print(f"{'ID':<5} {'Codigo':<10} {'Nombre':<25} {'Nota':<8} {'Creditos':<10}")
    print("-" * 63)
    
    for curso in cursos:
        print(f"{curso['id']:<5} {curso['codigo']:<10} {curso['nombre']:<25} {curso['nota']:<8.2f} {curso['creditos']:<10}")

def calcular_promedio():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    suma_ponderada = 0
    total_creditos = 0
    
    for curso in cursos:
        suma_ponderada += curso['nota'] * curso['creditos']
        total_creditos += curso['creditos']
    
    promedio = suma_ponderada / total_creditos
    print(f"\nPromedio ponderado general: {promedio:.2f}")
    historial.append("Calculado promedio general")

def contar_aprobados_reprobados():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    aprobados = sum(1 for curso in cursos if curso['nota'] >= 61)
    reprobados = len(cursos) - aprobados
    
    print(f"\nCursos aprobados (nota >= 61): {aprobados}")
    print(f"Cursos reprobados (nota < 61): {reprobados}")

# Funciones de busqueda

def buscar_por_nombre():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    nombre_buscar = input("\nIngrese el nombre del curso a buscar: ").strip()
    encontrado = False
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"\nCurso encontrado en posicion {i}:")
            print(f"ID: {cursos[i]['id']}")
            print(f"Codigo: {cursos[i]['codigo']}")
            print(f"Nombre: {cursos[i]['nombre']}")
            print(f"Nota: {cursos[i]['nota']}")
            print(f"Creditos: {cursos[i]['creditos']}")
            encontrado = True
            historial.append(f"Busqueda lineal: {nombre_buscar}")
            break
    
    if not encontrado:
        print("Curso no encontrado")

def buscar_por_codigo_binaria():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    print("Ordenando cursos por codigo para busqueda binaria...")
    ordenar_seleccion_por_codigo()
    
    codigo_buscar = input("\nIngrese el codigo del curso a buscar: ").strip().upper()
    
    izquierda = 0
    derecha = len(cursos) - 1
    encontrado = False
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if cursos[medio]['codigo'] == codigo_buscar:
            print(f"\nCurso encontrado en posicion {medio}:")
            print(f"ID: {cursos[medio]['id']}")
            print(f"Codigo: {cursos[medio]['codigo']}")
            print(f"Nombre: {cursos[medio]['nombre']}")
            print(f"Nota: {cursos[medio]['nota']}")
            print(f"Creditos: {cursos[medio]['creditos']}")
            encontrado = True
            historial.append(f"Busqueda binaria: {codigo_buscar}")
            break
        elif cursos[medio]['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    if not encontrado:
        print("Curso no encontrado")

# Funciones de actualizacion

def actualizar_nota():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    nombre_buscar = input("\nIngrese el nombre del curso a actualizar: ").strip()
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"\nCurso encontrado: {cursos[i]['nombre']}")
            print(f"Nota actual: {cursos[i]['nota']}")
            
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if not validar_nota(nueva_nota):
                    print("Error: La nota debe estar entre 0 y 100")
                    return
                
                nota_anterior = cursos[i]['nota']
                cursos[i]['nota'] = nueva_nota
                historial.append(f"Actualizada nota de {cursos[i]['nombre']}: {nota_anterior} -> {nueva_nota}")
                print("Nota actualizada exitosamente")
                return
            except ValueError:
                print("Error: Ingrese un numero valido")
                return
    
    print("Curso no encontrado")

def eliminar_curso():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    nombre_buscar = input("\nIngrese el nombre del curso a eliminar: ").strip()
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            curso_eliminado = cursos[i]
            historial.append(f"Eliminado curso: {curso_eliminado['nombre']} ({curso_eliminado['codigo']})")
            del cursos[i]
            print("Curso eliminado exitosamente")
            return
    
    print("Curso no encontrado")

# Algoritmos de ordenamiento

def ordenar_burbuja():
    n = len(cursos)
    if n == 0:
        print("\nNo hay cursos registrados")
        return
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if cursos[j]['nota'] > cursos[j + 1]['nota']:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    
    print("\nCursos ordenados por nota (Burbuja - menor a mayor)")
    historial.append("Ordenamiento burbuja por nota")

def ordenar_insercion():
    n = len(cursos)
    if n == 0:
        print("\nNo hay cursos registrados")
        return
    
    for i in range(1, n):
        key = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]['nombre'].lower() > key['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
    
    print("\nCursos ordenados por nombre (Insercion - alfabeticamente)")
    historial.append("Ordenamiento insercion por nombre")

def ordenar_seleccion_por_codigo():
    n = len(cursos)
    if n == 0:
        return
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if cursos[j]['codigo'].lower() < cursos[min_idx]['codigo'].lower():
                min_idx = j
        
        if min_idx != i:
            cursos[i], cursos[min_idx] = cursos[min_idx], cursos[i]
    
    print("\nCursos ordenados por codigo (Seleccion - alfabeticamente)")
    historial.append("Ordenamiento seleccion por codigo")

# Funciones de cola (FIFO)

def agregar_revision():
    if len(cursos) == 0:
        print("\nNo hay cursos registrados")
        return
    
    nombre = input("\nIngrese el nombre del curso a enviar a revision: ").strip()
    
    for curso in cursos:
        if curso['nombre'].lower() == nombre.lower():
            for c in cola_revision:
                if c['id'] == curso['id']:
                    print("Este curso ya esta en la cola de revision")
                    return
            
            cola_revision.append(curso)
            print(f"Curso '{nombre}' agregado a la cola de revision")
            historial.append(f"Agregado a revision: {nombre}")
            return
    
    print("Curso no encontrado")

def atender_revision():
    if len(cola_revision) == 0:
        print("\nNo hay cursos en la cola de revision")
        return
    
    curso = cola_revision.pop(0)
    print(f"\nAtendiendo revision del curso: {curso['nombre']}")
    print(f"Codigo: {curso['codigo']}")
    print(f"Nota actual: {curso['nota']}")
    historial.append(f"Atendida revision: {curso['nombre']}")

# Funciones de pila (LIFO)

def mostrar_historial():
    if len(historial) == 0:
        print("\nEl historial esta vacio")
        return
    
    print("\n--- HISTORIAL DE ACCIONES (ultimas primero) ---")
    
    for i in range(len(historial) - 1, -1, -1):
        print(f"{len(historial) - i}. {historial[i]}")

# Programa principal

def main():
    print("\n" + "="*50)
    print("  BIENVENIDO AL GESTOR DE NOTAS ACADEMICAS")
    print("="*50)
    
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
            buscar_por_codigo_binaria()
        elif opcion == 7:
            actualizar_nota()
        elif opcion == 8:
            eliminar_curso()
        elif opcion == 9:
            ordenar_burbuja()
        elif opcion == 10:
            ordenar_insercion()
        elif opcion == 11:
            ordenar_seleccion_por_codigo()
        elif opcion == 12:
            agregar_revision()
        elif opcion == 13:
            atender_revision()
        elif opcion == 14:
            mostrar_historial()
        elif opcion == 15:
            print("\nCerrando el sistema...")
            print("Gracias por usar el Gestor de Notas Academicas!")
            break
        else:
            print("\nOpcion invalida. Por favor ingrese una opcion valida (1-15).")
        
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
