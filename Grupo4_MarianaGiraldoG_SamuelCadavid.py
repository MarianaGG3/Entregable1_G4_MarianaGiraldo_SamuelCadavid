class Dispositivos:
    def __init__(self):
        self.__nombre=""
        self.__material=""
        self.__tamaño=0


class Protesiscadera(Dispositivos):
    pass


class Marcapasos(Dispositivos):
    pass

class Stents (Dispositivos):
    pass
class ImplantesDentales(Dispositivos):
    pass

class ProtesisRodilla(Dispositivos):
    pass

# def validar(msj):
#     while True:
#         try:
#             valor = int(input(msj))
#             break
#         except ValueError:
#             print("Ingrese un dato numérico...")

dispos=Dispositivos
while True:
    menu=int(input("""ingrese la opcion que dese seleccionar:
    1. Ingresar un nuevo implante
    2. Eliminar implante
    3. Editar información del implante 
    4. Visualizar el inventario completo
    5. Salir del sistema
    """))

    if menu==5:
        break
    elif menu==2:
        pass
    elif menu==3:
        pass
    elif menu==4:
        pass
    elif menu==1:
        pass

    else:
        print("ingrese una opcion")