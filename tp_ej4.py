"""ejercicio 4"""
"""Defino las variables necesarias para el juego de escape"""
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar = 0

print("¡Bienvenido al juego de escape!")
nombre = input("Ingrese su nombre: ")
while  not nombre.isalpha() or nombre == "":
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}! Tu objetivo es escapar de la habitación antes de que se acabe el tiempo.")
juego_activo = True
while cerraduras_abiertas < 3 and tiempo > 0 and energia > 0 and not alarma:
    
    print("\n" + "=" * 40)
    print(f"  Agente    : {nombre}")
    print(f"  Energia   : {energia}/100")
    print(f"  Tiempo    : {tiempo} turnos restantes")
    print(f"  Cerraduras: {cerraduras_abiertas}/3 abiertas")
    print(f"  Alarma    : {'ACTIVADA' if alarma else 'apagada'}")
    print(f"  Codigo    : {codigo_parcial if codigo_parcial != '' else '(vacío)'}")
    print("=" * 40)
    
    print("\n¿Qué quieres hacer?")
    print("1. Forzar una cerradura (-20 de energía, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3tiempo)")
    print("3. Descansar (+15 energia, -1 tiempo)")
    """Le pido al usuario que ingrese una opcion, lo valido con isdigit y luego uso un if para las opciones"""
    opcion = input("Selecciona una opción (1-4): ")
    while not opcion.isdigit() or opcion not in ['1', '2', '3', '4']:
        print("Error: Ingrese un número entre 1 y 4.")
        opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == '1':
        energia -= 20 
        tiempo -= 2
        contador_forzar += 1
        print(f"{nombre} has forzado una cerradura (-20 energia, -2 tiempo). Energía restante: {energia}. Tiempo restante: {tiempo}.")
        
        if contador_forzar >= 3:
            alarma = True
            contador_forzar = 0
            print("¡Alarma activada! Has forzado demasiadas cerraduras.")
        else:
            if energia < 40:
                print("¡Cuidado! Tu energía está baja. Riesgo de alarma .")
                riego =  input("Elige una opción: 1. Continuar forzando, 2. Descansar: ")
                if riego == '3':
                    alarma = True
                    print("¡Alarma activada! Has decidido continuar forzando con energía baja.")
                else:
                    cerraduras_abiertas += 1
                    print(f"¡Cerradura abierta! Cerraduras abiertas: {cerraduras_abiertas}/3.")
            else:
                cerraduras_abiertas += 1
                print(f"¡Cerradura abierta! Cerraduras abiertas: {cerraduras_abiertas}/3.")
    elif opcion == '2':
        energia -= 10
        tiempo -= 3
        contador_forzar=0
        print(f"{nombre} has hackeado el panel (-10 energia, -3 tiempo). Energía restante: {energia}. Tiempo restante: {tiempo}.")
        for paso in range (1, 4):
            codigo_parcial += "A"   
            print(f"Hackeando... Paso {paso}/3. codifico parcial: {codigo_parcial}")
            if len(codigo_parcial) >=8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f"¡Cerradura abierta! Cerraduras abiertas: {cerraduras_abiertas}/3.")
                
        
    elif opcion == '3':
        tiempo -= 1
        contador_forzar=0
        
        if alarma:
            energia -= 10
            print(f"{nombre} has descansado pero la alarma está activada (-10 energia, -1 tiempo). Energía restante: {energia}. Tiempo restante: {tiempo}.")
        else:
            energia += 15
            if energia > 100:
                energia = 100
            print(f"{nombre} has descansado (+15 energia, -1 tiempo). Energía restante: {energia}. Tiempo restante: {tiempo}.")
        
        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            print("¡Alerta! La alarma está activada y el tiempo se está agotando. ¡Debes actuar rápido!")

if cerraduras_abiertas == 3:
    print(f"¡Felicidades, {nombre}! Has abierto las 3 cerraduras y escapado de la habitación.")
elif alarma and tiempo <= 3:
    print(f"¡Tiempo agotado, {nombre}! La alarma se ha activado y no has logrado escapar.")
elif energia <= 0:
    print(f"¡Energía agotada, {nombre}! No has logrado escapar.")
elif tiempo <= 0:
    print(f"¡Tiempo agotado, {nombre}! No has logrado escapar.")
    
print ("Estadisticas finales:")
print(f"  Jugador: {nombre}")
print(f"  Cerraduras abiertas: {cerraduras_abiertas}/3")
print(f"  Energía final: {energia}/100")
print(f"  Tiempo final: {tiempo} turnos")