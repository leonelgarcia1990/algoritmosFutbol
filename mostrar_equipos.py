def mostrar_equipos(lista_equipos):

 print("\nLista de equipos:")
 for i in range(len(lista_equipos)):
     print(f"{i+1}. {lista_equipos[i]}")
     
# Imprime el número de equipo seguido del nombre del equipo

# i+1: Muestra la numeración desde 1 en lugar de 0 (más natural para usuarios)

# lista_equipos[i]: Accede al elemento en la posición i de la lista

# usamos una f string la f permite insertar el valor de i+1 
# y el elemento lista_equipos[i] directamente en la cadena que se va a imprimir.

    