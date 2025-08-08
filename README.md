# Gestor de Notas Académicas

## Redacción del Problema

El Gestor de Notas Académicas es un sistema diseñado para ayudar a estudiantes universitarios y de educación superior a organizar, administrar y hacer seguimiento de sus calificaciones de manera eficiente. En el entorno académico actual, los estudiantes manejan múltiples cursos simultáneamente, cada uno con diferentes tipos de evaluaciones, ponderaciones y escalas de calificación, lo que hace complejo mantener un registro ordenado y actualizado de su rendimiento académico.

Este sistema está dirigido principalmente a estudiantes que necesitan una herramienta simple pero efectiva para registrar sus notas, calcular promedios, identificar materias con bajo rendimiento y tener una visión integral de su progreso académico. La aplicación busca cubrir la necesidad de centralizar la información académica en una interfaz de fácil uso, permitiendo a los usuarios tomar decisiones informadas sobre su desempeño estudiantil.

El objetivo principal es proporcionar una solución práctica que permita a los estudiantes gestionar sus calificaciones de forma organizada, realizar cálculos automáticos de promedios y obtener reportes que les ayuden a identificar áreas de mejora en su rendimiento académico, todo esto a través de una interfaz de consola intuitiva y accesible.

## Requisitos del Sistema

### Requisitos Funcionales

1. **Registrar nuevo curso y nota**: El sistema debe permitir al usuario agregar nuevos cursos con sus respectivas calificaciones, incluyendo nombre del curso, tipo de evaluación, nota obtenida y ponderación.

2. **Mostrar todas las notas registradas**: El sistema debe ser capaz de mostrar un listado completo de todos los cursos y notas almacenadas, organizadas de manera clara y legible para el usuario.

3. **Calcular promedio general**: El sistema debe calcular automáticamente el promedio ponderado de todas las materias registradas, considerando los créditos o ponderaciones asignadas a cada curso.

4. **Buscar notas por curso**: El sistema debe permitir al usuario buscar y visualizar las calificaciones de un curso específico, mostrando todas las evaluaciones registradas para esa materia.

5. **Generar reporte de rendimiento**: El sistema debe generar un reporte que muestre las materias con mejor y peor rendimiento, identificando aquellas que requieren mayor atención académica.

### Requisitos No Funcionales

- El sistema se ejecutará completamente en consola utilizando Python como lenguaje de programación.
- No se utilizarán librerías externas, solo las funciones básicas integradas de Python.
- La implementación debe incluir estructuras de control como bucles y condicionales expresados en pseudocódigo.
- La interfaz debe ser intuitiva y fácil de navegar para usuarios sin experiencia técnica.
- El sistema debe mantener la persistencia de datos durante la sesión de ejecución.
- Los cálculos deben ser precisos y mostrar resultados con formato decimal apropiado.
