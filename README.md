# 📚 Gestor de Notas Académicas

## Redacción del Problema
En la vida universitaria es común llevar varios cursos al mismo tiempo, cada uno con tareas, exámenes, laboratorios y distintas ponderaciones. Esto puede volver complicado el control de las calificaciones y del promedio general.  

El **Gestor de Notas Académicas** es un programa desarrollado en Python que permite registrar cursos, almacenar sus evaluaciones con sus respectivas ponderaciones, calcular promedios y generar reportes de rendimiento. Todo esto se realiza de forma sencilla desde la consola, sin depender de hojas de cálculo ni software adicional.  

Este sistema está pensado para estudiantes que necesitan organizar sus notas y tener una visión clara de su avance académico, identificando de manera rápida cuáles son sus puntos fuertes y en qué materias necesitan mejorar.

---

##  Requisitos Funcionales
El menú del sistema debe incluir al menos las siguientes funciones:  
1. **Registrar nuevo curso y nota** con nombre, tipo de evaluación, nota obtenida y ponderación.  
2. **Mostrar todas las notas registradas** de forma clara y ordenada.  
3. **Calcular el promedio general ponderado** de todas las materias.  
4. **Buscar notas por curso** para consultar el detalle de una materia específica.  

---

## Requisitos No Funcionales
- El sistema se desarrollará **exclusivamente en Python**.  
- Ejecución únicamente por **línea de comandos** (consola).  
- **No** se permite el uso de librerías externas, solo funciones y estructuras básicas de Python.  
- Debe implementar **bucles** y **condicionales** según el pseudocódigo diseñado.  


📘 Explicación del proyecto

En este avance del proyecto se implementaron las siguientes mejoras:

🗂 Uso de listas

Se utilizó una lista para almacenar los cursos registrados, lo cual permite manejar múltiples elementos de manera dinámica (agregar, mostrar y eliminar cursos).
Esto facilita la gestión de los datos sin necesidad de usar estructuras más complejas.

⚙️ Funciones

Se organizó el código en funciones para dividir el programa en tareas específicas y reutilizables.
Por ejemplo:

agregar_curso() para registrar un nuevo curso.

mostrar_cursos() para listar los cursos existentes.

eliminar_curso() para borrar un curso de la lista.

Esto mejora la legibilidad, el mantenimiento y la reutilización del código.

🧩 Modularización

El código se dividió en módulos (archivos .py separados) para organizar mejor las diferentes partes del programa.
Por ejemplo, un archivo puede contener la lógica de los cursos y otro el archivo principal que ejecuta el programa.
Esto facilita trabajar en equipo y mantener el proyecto conforme crece.

🗑 Eliminación de cursos

Se añadió la función de eliminar cursos que permite al usuario seleccionar un curso específico y quitarlo de la lista.
Esto hace que el sistema sea más flexible y realista, ya que los cursos pueden cambiar con el tiempo.
