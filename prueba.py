print("Hola, Usuario!")

#creacion de cuenta del usuario
usuario = input("Por favor, ingresa tu nombre: ")
if usuario == "":
    print("No ingresaste un nombre.")
else:
    print(f"¡Hola, {usuario}! Bienvenido/a al programa.")

nombre_de_usuario = input("Por favor, crea un nombre de usuario: ")
if nombre_de_usuario == "":
    print("No ingresaste un nombre de usuario.")
else:
    print(f"Nombre de usuario '{nombre_de_usuario}' registrado.")

contraseña_nueva = input("Por favor, crea una nueva contraseña: ")
if contraseña_nueva == "":
    print("No ingresaste una nueva contraseña.")
else:
    print("Nueva contraseña registrada.")

contraseña = input("Por favor, ingresa tu contraseña: ")
if contraseña == "":
    print("No ingresaste una contraseña.")
else:
    print("Contraseña registrada.")

#cuestionario de preguntas
print("Ahora, vamos a hacer un pequeño cuestionario.")
color_favorito = input("Pregunta 1: ¿Cuál es tu color favorito? ")
if color_favorito == "":
    print("No ingresaste un color favorito.")
else:
    print(f"Tu color favorito es {color_favorito}.")

peliculas_favoritas = input("Pregunta 2: ¿Cuáles son tus 3 películas favoritas? (separadas por comas) ")
if peliculas_favoritas == "":
    print("No ingresaste tus películas favoritas.")
else:
    peliculas = [pelicula.strip() for pelicula in peliculas_favoritas.split(",")]
    print(f"Tus películas favoritas son: {', '.join(peliculas)}.")






