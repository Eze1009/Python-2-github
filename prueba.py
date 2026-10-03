print("Hola, Usuario!")

usuario = input("Por favor, ingresa tu nombre: ")
if usuario == "":
    print("No ingresaste un nombre.")
else:
    print(f"¡Hola, {usuario}! Bienvenido/a al programa.")

contraseña = input("Por favor, ingresa tu contraseña: ")
if contraseña == "":
    print("No ingresaste una contraseña.")
else:
    print("Contraseña registrada.")