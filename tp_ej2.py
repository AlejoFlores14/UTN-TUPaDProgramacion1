"""ejercicio 2 -- acceso al campus y menu seguro"""
"""Defino usuario correcto y contraseña correcta"""
usuario_correcto = "alumno"
contraseña_correcta = "python123"
"""le pido al ususario que ingrese su usuario y contraseña, y le doy 3 intentos para ingresar correctamente"""
intentos = 0
acceso_concedido = False
for i in range(intentos , 3):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        acceso_concedido = True
        break
    else:
        print(f"Usuario o contraseña incorrectos. Intento {i + 1} de 3.")
"""Si la contraseña es correcta, entonces acceso_consedido es true y muestra el menu"""
if acceso_concedido:
    while True:
        print("¡Bienvenido al campus virtual!")
        print("Menú de opciones:")
        print("1. Estado de la inscripción")
        print("2. cambiar contraseña")
        print("3. Mensaje")
        print("4. Salir")
        """le pido al usuario que eliga una opcion del menu y verifico que la respuesta sea correcta en cuanto las opciones """
        opcion = input("Seleccione una opción (1-4): ")
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: Ingrese un número entre 1 y 4.")
            opcion = input("Seleccione una opción (1-4): ")
        opcion = int(opcion)
        """mediasnte un if muestro la respuesta que eligio el usuario en el menu"""
        if opcion == 1:
            print("----Su inscripción está activa.----")
        elif opcion == 2:
            nueva_contraseña = (input("Ingrese la nueva contraseña: "))
            if len(nueva_contraseña) < 6:
                print("La contraseña debe tener un minimo de 6 caracteres ")
                nueva_contraseña = (input("Ingrese la nueva contraseña: "))
            else: 
                print("Contraseña cambiada correcatamente! ")
        elif opcion == 3:
            print("---mensaje motivacional capo----")
        elif opcion == 4:
            print("¡Hasta luego!")
            break

    