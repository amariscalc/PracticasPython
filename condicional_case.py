# Condicional match;case

'''
Inicializamos algunas variables pidiendo datos. 
Transformamos la plataforma introducida por el usuario a minúsculas por que desconocemos como el usuario
la va a introducir.
'''
nombre_usuario = input ("Introduce tu nombre: ")
plataforma = input ("Introduce tu plataforma de juego favorita PC/XBOX/PlayStation/Switch: ")

match str.lower(plataforma):
    case "pc":
        print("Bravo! Otro más que se apunta a la Master Racer!!!")
    case "xbox":
        print("Nada como un buen Gears of Wars.")
    case "playstation":
        print("Para vosotros, jugadores. Los mejores exclusivos.")
    case "switch":
        print("Nada como ir de aventuras con Mario, Luigi... o ayudar a Link y Zelda a salvar Hyrule...")
    case _:
        print("Plataforma no reconocida.")
