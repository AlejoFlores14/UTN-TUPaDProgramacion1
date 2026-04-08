"""EJERCICIO 5"""
"""Pido nombre del gladeador y luego verifico con isalpha()"""
gladiador = input("Ingrese el nombre del gladeador ")
while not gladiador.isalpha() or gladiador == "":
    print ("Solo debe contener letras ")
    gladiador = input("Ingrese el nombre del gladeador ")
"""Defino las variables """
vida_gladeador = int(100)
vida_enemigo = int(100)
pociones = int(3)
ataque_pesado = int(15)
daño_enemigo = int(12)
turno_gladeador = True
print("---- BIENVENIDO A LA ARENA ----")    
print(f"Nombre del gladeador: {gladiador}")
"""mientras vida del enemigo y del gladeador sean mayores a 0, se ejecuta el juego"""
while vida_enemigo > 0 and vida_gladeador > 0:
    """turno del gladeador es igual a True, para manejar los turnos"""
    if turno_gladeador:
        print(f"{gladiador}: (HP:{vida_gladeador}) vs Enemigo: (HP:{vida_enemigo}) | Pociones: {pociones}")
        print(f"Elije accion:")
        print("1. Ataque pesado")
        print("2. rafaga veloz")
        print("3. curar")
        opcion = input("Selecciona una opción (1-3): ")  
        print(f"Opción: {opcion}.")
        """pido que opcion va a elegir el gladeador y luego aplico el daño segun la opcion, despues turno_gladeador es igual a false y automaticamente el enmigo contraataca """
        while not opcion.isdigit() or opcion not in ['1', '2', '3']:
            print("Error: Ingrese un número entre 1 y 3.")
            opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1':
            if vida_enemigo < 20:
                critico = ataque_pesado * 1.5
                vida_enemigo -= critico
                print(f"Atacaste al enemigo por {critico} puntos de daño.")
            else:
                vida_enemigo -= ataque_pesado
                print(f"Atacaste al enemigo por {ataque_pesado} puntos de daño.")
        elif opcion == '2':
            for i in range(3):
                vida_enemigo -= 5 
                print(f"Atacaste al enemigo por 5 puntos de daño.")
        elif opcion == '3':
            if pociones > 0:
                vida_gladeador += 30
                pociones -= 1
                print(f"Usaste una poción y recuperaste 30 puntos de vida. Vida actual: {vida_gladeador}. Pociones restantes: {pociones}.")
            else:
                print("No te quedan pociones.")
        turno_gladeador = False
    else:
        vida_gladeador -= daño_enemigo
        print(f"El enemigo te atacó por {daño_enemigo} puntos de daño.")
        turno_gladeador = True
        print("==== NUEVO TURNO ====")
"""Al finalizar el juego, se muestra un mensaje dependiendo de quien gane"""
if vida_gladeador > 0:
    print(f"¡VICTORIA {gladiador}, ha ganado la batalla!")
else:
    print(f"¡DERROTA, has caido en combate!")