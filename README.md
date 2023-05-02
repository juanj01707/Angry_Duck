# **Angry_Duck**
es un programa que realiza cálculos y simulaciones para determinar la distancia recorrida por un proyectil en un tiro parabólico.

## **-Estos son los pasos que sigue el algoritmo**
1. Importa el módulo math para utilizar funciones matemáticas.
2. Define la función  "calcular_distancia_tiro_parabolico" que toma cuatro parámetros: h (altura de la honda), p1 (punto de referencia 1), p2 (punto de referencia 2) y n (número de casos de prueba).
3. Dentro de la función, se define una constante PI  y otra constante G .
4. Iniciar un bucle for para iterar n veces.
5. Dentro del bucle, se solicita al usuario que ingrese el ángulo de disparo (alfa) y la velocidad de lanzamiento (v).
6. Convertir el ángulo de disparo a radianes.
7. Se calcula la componente horizontal de la velocidad inicial (Vox) utilizando la función coseno de math.cos.
8. Se calcula la componente vertical de la velocidad inicial (Voy) utilizando la función seno de math.sin.
9. Se calcula el tiempo de subida (Ts) dividiendo la componente vertical de la velocidad inicial entre la constante G.
10. Se calcula la altura máxima alcanzada (H) utilizando la fórmula de la posición vertical de un proyectil en tiro parabólico.
11. Se calcula la velocidad final en el eje vertical (Vfy) utilizando la fórmula de la velocidad final en caída libre.
12. Se calcula el tiempo de descenso (Td) dividiendo la velocidad final en el eje vertical entre la constante G.
13. Se calcula el tiempo total de vuelo (Tt) sumando el tiempo de subida y el tiempo de descenso.
14. Se calcula la distancia recorrida (D) multiplicando la componente horizontal de la velocidad inicial por el tiempo total de vuelo.
15. Se verifica si la distancia recorrida está entre los puntos de referencia p1 y p2.
16. Se muestra en pantalla la distancia recorrida y un mensaje indicando si el proyectil alcanza o no a un objetivo (pato) en función de los puntos de referencia.
17. Se define una función llamada "main" que realiza lo siguiente:
 + a. Solicita al usuario que ingrese la altura de la honda, el punto de referencia p1, el punto de referencia p2 y el número de casos de prueba.
 + b. Llama a la función "calcular_distancia_tiro_parabolico" pasando los valores ingresados por el usuario como argumentos.
