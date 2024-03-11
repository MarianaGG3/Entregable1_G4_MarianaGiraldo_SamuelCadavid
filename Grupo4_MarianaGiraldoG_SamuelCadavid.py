class Implantes: #Clase padre de Implantes
    def __init__(self, precio, distribuidor, estado ):
        
        self.__precio=precio
        self.__distribuidor=distribuidor
        self.__estado=estado


class Protesiscadera(Implantes):
   def __init__(self, precio, distribuidor, estado, tipofij, tamano, material):
        super().__init__(self, precio, distribuidor, estado)
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material
        

class Marcapasos(Implantes):
    def __init__(self, precio, distribuidor, estado, frec, nelectrodos, alambrico):
        super().__init__(self, precio, distribuidor, estado)
        self.__distribuidor=distribuidor
        self.__estado=estado
        self.__frec=frec
        self.__nelectrodos=nelectrodos
        self.__alambrico=alambrico



class Stents (Implantes):
    def __init__(self, precio, distribuidor, estado, longitud, diametro, material):
        super().__init__(self, precio, distribuidor, estado)
        self.__longitud=longitud
        self.__diametro=diametro
        self.__material=material




class ImplantesDentales(Implantes):
    def __init__(self, precio, distribuidor, estado, forma, sistfij, material):
        super().__init__(self, precio, distribuidor, estado)
        self.__forma=forma
        self.__sistfij=sistfij
        self.__material= material



class ProtesisRodilla(Implantes):
    def __init__(self, precio, distribuidor, estado, tipofij, tamano, material):
        super().__init__(self, precio, distribuidor, estado)
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material


# def validar(msj):
#     while True:
#         try:
#             valor = int(input(msj))
#             break
#         except ValueError:
#             print("Ingrese un dato numérico...")

imp=Implantes
while True:
    menu=int(input("""ingrese la opcion que dese seleccionar:
    1. Ingresar un nuevo implante
    2. Eliminar implante
    3. Editar información del implante 
    4. Visualizar el inventario completo
    5. Salir del sistema
    """))

    if menu==1:
        pass
    elif menu==2:
        pass
    elif menu==3:
        pass
    elif menu==4:
        pass
    elif menu==5:
        break

    else:
        print("ingrese una opcion")