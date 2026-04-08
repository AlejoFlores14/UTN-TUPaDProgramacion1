""" Ejercicio  3"""
"""Inicio las variables por dia y turno """
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
"""pido el nombre y valido"""
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha() or nombre == "":
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese su nombre: ")

opcion = ""
"""hago un while para que se muestre el menu hasta que el usuario elija salir"""
while opcion != "5":
    print("BIENVENIDO")
    print("1.- Reservar turno")
    print("2.- Cancelar turno")
    print("3.- Ver agenda del dia")
    print("4.- Ver resumen general ")
    print("5.- Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    """if para manejar el menu, y que dependiendo de la opcion se ejecute lo que elijio el usuario"""
    if opcion == "1":
        print("Seleccione un día para reservar turno:")
        print("1. Lunes")
        print("2. Martes")
        dia = input("Ingrese el número del día (1-2): ")
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not nombre_paciente.isalpha() or nombre_paciente == "":
            print("Error: El nombre del paciente debe contener solo letras y no estar vacío.")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
        if dia == "1":
            if nombre_paciente in [lunes1, lunes2, lunes3, lunes4]:
                print(f"Error: El paciente {nombre_paciente} ya tiene un turno reservado el lunes.")
            elif lunes1 == "":
                lunes1 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes en el horario 9:00-10:00.")
            elif lunes2 == "":
                lunes2 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes en el horario 10:00-11:00.")
            elif lunes3 == "":
                lunes3 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes en el horario 11:00-12:00.")
            elif lunes4 == "":
                lunes4 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes en el horario 12:00-13:00.")
            else:
                print("Lo siento, no hay turnos disponibles para el lunes.")
        elif dia == "2":
            if nombre_paciente in [martes1, martes2, martes3]:
                print(f"Error: El paciente {nombre_paciente} ya tiene un turno reservado el martes.")
            elif martes1 == "":
                martes1 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes en el horario 9:00-10:00.")
            elif martes2 == "":
                martes2 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes en el horario 10:00-11:00.")
            elif martes3 == "":
                martes3 = nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes en el horario 11:00-12:00.")
            else:
                print("Lo siento, no hay turnos disponibles para el martes.")
        else:
            print("Opción de día inválida. Por favor, seleccione 1 o 2.")
    elif opcion == "2":
        print("Seleccione un día para cancelar turno:")
        print("1. Lunes")
        print("2. Martes")
        dia = input("Ingrese el número del día (1-2): ")
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not nombre_paciente.isalpha() or nombre_paciente == "":     
            print("Error: El nombre del paciente debe contener solo letras y no estar vacío.")
            nombre_paciente = input("Ingrese el nombre del paciente: ")
        if dia == "1":
            if lunes1 == nombre_paciente:
                lunes1 = ""
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 9:00-10:00.")
            elif lunes2 == nombre_paciente:
                lunes2 = ""
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 10:00-11:00.")
            elif lunes3 == nombre_paciente:
                lunes3 = ""
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 11:00-12:00.")
            elif lunes4 == nombre_paciente:
                lunes4 = ""
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 12:00-13:00.")
            else:
                print("No se encontró un turno reservado a su nombre para el lunes.")
        elif dia == "2":
            if martes1 == nombre_paciente:
                martes1 = ""
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 9:00-10:00.")
            elif martes2 == nombre_paciente:
                martes2 = ""
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 10:00-11:00.")
            elif martes3 == nombre_paciente:
                martes3 = ""
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 11:00-12:00.")
            else:
                print("No se encontró un turno reservado a su nombre para el martes.")
        else:
            print("Opción de día inválida. Por favor, seleccione 1 o 2.")
    elif opcion == "3":
        dia = input("Seleccione un día para ver la agenda (1. Lunes, 2. Martes): ")
        if dia == "1":
            print("Agenda del lunes:")
            print(f"9:00-10:00: {lunes1 if lunes1 else 'Disponible'}")
            print(f"10:00-11:00: {lunes2 if lunes2 else 'Disponible'}")
            print(f"11:00-12:00: {lunes3 if lunes3 else 'Disponible'}")
            print(f"12:00-13:00: {lunes4 if lunes4 else 'Disponible'}")
        elif dia == "2":
            print("Agenda del martes:")
            print(f"9:00-10:00: {martes1 if martes1 else 'Disponible'}")
            print(f"10:00-11:00: {martes2 if martes2 else 'Disponible'}")
            print(f"11:00-12:00: {martes3 if martes3 else 'Disponible'}")
        else:
            print("Opción de día inválida. Por favor, seleccione 1 o 2.")
    elif opcion == "4":
        lunes_ocupados = sum(1 for turno in [lunes1, lunes2, lunes3, lunes4] if turno)
        martes_ocupados = sum(1 for turno in [martes1, martes2, martes3] if turno)
        libre_lunes = 4 - lunes_ocupados
        libre_martes = 3 - martes_ocupados
        print(f"Turnos disponibles - Lunes: {libre_lunes}, Martes: {libre_martes}")
        print(f"Turnos ocupados - Lunes: {lunes_ocupados}, Martes: {martes_ocupados}")
        
        if lunes_ocupados > martes_ocupados:
            print("El día con más turnos ocupados es el lunes.")
        elif martes_ocupados > lunes_ocupados:
            print("El día con más turnos ocupados es el martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")
    elif opcion == "5":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione un número entre 1 y 5.")