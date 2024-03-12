class Implantes: #Clase padre de Implantes

    #constructor que inicializa la clase implantes
    def __init__(self, precio, distribuidor, estado ):


    #atributos privados   
        self.__precio=precio
        self.__distribuidor=distribuidor
        self.__estado=estado

        #getters: permiten ver los objetos de la clase

        def verPrecio(self):
            return self.__precio

        def verDistribuidor(self):
            return self.__distribuidor
        
        def verEstado(self):
            return self.__estado
        
        #setter: asignan los objetos
        def asignarPrecio (self, precio):
            self.__precio= precio

        def asignarDistribuidor (self, distribuidor):
            self.__distribuidor=distribuidor
        
        def asignarEstado (self, estado):
            self.__estado=estado

class Protesiscadera(Implantes):
   def __init__(self, precio, distribuidor, estado, tipofij, tamano, material):
    #constructor que llama los atributos de la clase padre
        super().__init__(self, precio, distribuidor, estado)
        #atributos privados
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material

        #getters de la clase protesis cadera:

        def verTipofij(self):
            return self.__tipofij

        def verTamano(self):
            return self.__tamano

        def verMaterial(self):
            return self.__material
    
        #setters: asignacion de los atributos 

        def asignarTipofij (self, tipofij):
            self.__tipofij=tipofij

        def asignarTamano (self, tamano):
            self.__tamano=tamano

        def asignarMaterial (self, material):
            self.__material=material
        

class Marcapasos(Implantes):
    def __init__(self, precio, distribuidor, estado, frec, nelectrodos, alambrico):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, precio, distribuidor, estado)
        #atributos privados
        self.__frec=frec
        self.__nelectrodos=nelectrodos
        self.__alambrico=alambrico


    # getters
        def verFrec(self):
            return self.__frec

        def verNElectrodos(self):
            return self.__nelectrodos
        def verAlamb(self):
            return self.__alambrico

    #setters

        def asignarFrec (self, frec):
            self.__frec=frec

        def asignarNElectrodos (self, nelectrodos):
            self.__nelectrodos=nelectrodos

        def asignarAlamb (self, alambrico):
            self.__alambrico=alambrico
    

class Stents (Implantes):
    def __init__(self, precio, distribuidor, estado, longitud, diametro, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, precio, distribuidor, estado)
        #atributos privados
        self.__longitud=longitud
        self.__diametro=diametro
        self.__material=material

    #getters

    def verLong(self):
            return self.__longitud
     
    def verDiam(self):
            return self.__diametro

    def verMaterial(self):
            return self.__material

    #setters

    def asignarLong (self, longitud):
            self.__longitud=longitud

    def asignarDiam (self, diametro):
            self.__diametro=diametro


    def asignarMaterial (self, material):
            self.__material=material

class ImplantesDentales(Implantes):
    def __init__(self, precio, distribuidor, estado, forma, sistfij, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, precio, distribuidor, estado)
        #atributos privados
        self.__forma=forma
        self.__sistfij=sistfij
        self.__material= material

        #getters

    def verForma(self):
            return self.__forma
    
    def verSistFij(self):
            return self.__sistfij
    
    def verMaterial(self):
            return self.__material

        #setters

    def asignarForma (self, forma):
            self.__forma=forma

    def asignarSistFij (self, sistfij):
            self.__sistfij=sistfij

    def asignarMaterial (self, material):
            self.__material=material

class ProtesisRodilla(Implantes):
    def __init__(self, precio, distribuidor, estado, tipofij, tamano, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, precio, distribuidor, estado)
        #atributos privados
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material

        #getters

    def verTipofij(self):
            return self.__tipofij

    def verTamano(self):
            return self.__tamano

    def verMaterial(self):
            return self.__material

        #setters

    def asignarTipofij (self, tipofij):
            self.__tipofij=tipofij

    def asignarTamano (self, tamano):
            self.__tamano=tamano

    def asignarMaterial (self, material):
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