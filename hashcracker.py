"Decifrador de hashes SHA-256 utilizando un ataque de diccionario."

# Este programa intenta encontrar la contraseña original correspondiente a un hash SHA-256 dado
# utilizando un archivo de diccionario que contiene posibles contraseñas.

import hashlib                                                                  # Importar la biblioteca hashlib para funciones de hash

hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"  # Ejemplo de hash SHA-256 para "test"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")          # Ruta del archivo del diccionario

with open(dic_file, 'r') as file:                                               # Abrir el archivo del diccionario

    diccionario = [line.strip() for line in file]                               # Leer las líneas y eliminar espacios en blanco

    for password in diccionario:                                                # Iterar sobre cada contraseña en el diccionario

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()          # Calcular el hash SHA-256 de la contraseña

        if hash_calculado == hash_file:                                         # Comparar el hash calculado con el hash objetivo

            print("¡Contraseña encontrada! La contraseña es: " + password)      # Imprimir la contraseña encontrada
            break                                                               # Salir del bucle si se encuentra la contraseña
    
    else:                                                                       # Si no se encuentra la contraseña en el diccionario

        print("Contraseña no encontrada en el diccionario.")                    # Imprimir mensaje de no encontrada

