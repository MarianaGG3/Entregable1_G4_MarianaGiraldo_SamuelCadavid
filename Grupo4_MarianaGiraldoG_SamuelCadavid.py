import datetime

class Implantes: #Clase padre de Implantes

    #constructor que inicializa la clase implantes
    def __init__(self, medico, fecha, estado, cantidad, cedula ):


    #atributos privados   
        self.__fecha=fecha
        self.__medico=medico
        self.__estado=estado
        self.__cantidad=cantidad
        self.__cedula=cedula
    #getters: permiten ver los objetos de la clase

        def verMedico(self):
            return self.__medico

        def verFecha(self):
            return self.__fecha
        
        def verEstado(self):
            return self.__estado
        
        def verCantidad(self):
            return self.__cantidad
        def vercedula(self):
             return self.__cedula

        #setter: asignan los objetos
        def asignarMedico (self, medico):
            self.__medico= medico

        def asignarFecha (self, fecha):
            self.__fecha=fecha
        
        def asignarEstado (self, estado):
            self.__estado=estado
        
        def asignarCantidad(self, cantidad):
            self.__cantidad=cantidad
        def asignarCedula(self,cedula):
             self.__cedula=cedula
class Protesiscadera(Implantes):
   def __init__(self,  medico, fecha, estado,cantidad,cedula, tipofij, tamano, material):
    #constructor que llama los atributos de la clase padre
        super().__init__(self, medico, fecha, estado, cantidad, cedula)
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
    def __init__(self,  medico, fecha, estado, cantidad,cedula, frec, nelectrodos, alambrico):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, medico, fecha, estado, cantidad,cedula)
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
    def __init__(self,  medico, fecha, estado, cantidad,cedula, longitud, diametro, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self,  medico, fecha, estado,cantidad,cedula)
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
    def __init__(self,  medico, fecha, estado, cantidad,cedula, forma, sistfij, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self, medico, fecha, estado, cantidad,cedula)
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
    def __init__(self,  medico, fecha,estado, cantidad,cedula, tipofij, tamano, material):
        #constructor que llama los atributos de la clase padre
        super().__init__(self,  medico, fecha, estado, cantidad)
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

class Sistema():
    def __init__(self):
        self.__listaimplantes=[]

    def agregarImplante(self, implante):
        self.__listaimplantes.append(implante)

    def verImplante(self):
        for i in self.__listaimplantes:
            pass
    def nuevo_implante(self,cedula,nuevo_implante):
         implante_encontrado= None
         for i, cedula in enumerate(self.__listaimplantes):
              if cedula in self.__listaimplantes:
                   implante_encontrado=i
                   break
         if implante_encontrado is not None:
              self.__listaimplantes[implante_encontrado]= nuevo_implante
              print(f"implante con cedula {cedula} actualizada ")
              print(implante_encontrado)
         else:
              print(f"No se encontro implante con cedula {cedula}")

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
        id_pac=int(input("ingrese el documento del paciente: "))
        tipoimp=int(input("""ingrese el implante a ingresar:
        1. protesis cadera
        2. marcapasos
        3. stents
        4. implantes dentales
        5. protesis rodilla
        :  """))
        if tipoimp==1:
            medico=int(input("ingrese identificacion del medico responsable: "))
            fecha=input("ingrese fecha:  ")
            estado=input("ingrese estado del implante:")
            cantidad= input("ingrese cantidad:")
            cedula=int(input("ingrese la cedula del paciente"))
            tipofij=input("ingrese tipo de fijacion:")
            tamano=input("ingrese tamaño:")
            material=input("ingrese material:")
            pc=Protesiscadera(medico, fecha, estado,cantidad,cedula, tipofij, tamano, material)
            Sistema.agregarImplante(pc)
            
        elif tipoimp==2:
            medico=int(input("ingrese identificacion del medico responsable: "))
            fecha=input("ingrese fecha:  ")
            estado=input("ingrese estado del implante:")
            cantidad= input("ingrese cantidad:")
            cedula=int(input("ingrese la cedula del paciente"))
            frec=("ingrese frecuencia de estimulacion: ")
            nelectrodos=("ingrese numero de electrodos: ")
            alambrico=("ingrese si es alambrico o inalambrico: ")
            mp=Marcapasos(medico, fecha, estado, cantidad,cedula, frec, nelectrodos, alambrico)
            Sistema.agregarImplante(mp)

        elif tipoimp==3:
            medico=int(input("ingrese identificacion del medico responsable: "))
            fecha=input("ingrese fecha:  ")
            estado=input("ingrese estado del implante:")
            cantidad= input("ingrese cantidad:")
            cedula=int(input("ingrese la cedula del paciente"))
            longitud=("ingrese longitud :")
            diametro=("ingrese diametro:")
            material=("ingrese material:")
            s=Stents(medico, fecha, estado, cantidad,cedula, longitud, diametro, material)
            Sistema.agregarImplante(s)
        elif tipoimp==4:
            medico=int(input("ingrese identificacion del medico responsable: "))
            fecha=input("ingrese fecha:  ")
            estado=input("ingrese estado del implante:")
            cantidad= input("ingrese cantidad:")
            cedula=int(input("ingrese la cedula del paciente"))
            forma= input("ingrese forma: ")
            sistfij= input("ingrese sistema de fijacion: ")
            material= input("ingrese material: ")
            id=ImplantesDentales(medico, fecha, estado, cantidad, cedula, forma, sistfij, material)
        elif tipoimp==5:
            medico=int(input("ingrese identificacion del medico responsable: "))
            fecha=input("ingrese fecha:  ")
            estado=input("ingrese estado del implante:")
            cantidad= input("ingrese cantidad:")
            cedula=int(input("ingrese la cedula del paciente"))
            tipofij=input("ingrese tipo de fijacion:")
            tamano=input("ingrese tamaño:")
            material=input("ingrese material:")
            pr=ProtesisRodilla(medico, fecha, estado, cantidad, cedula, tipofij, tamano, material)

        
        else:
            continue
    elif menu==2:
        pass
    elif menu==3:
        cedula("ingrese la cedula del paciente con el implante a editar")
        nuevo_implante=int(input("""ingrese el implante a ingresar:
        1. protesis cadera
        2. marcapasos
        3. stents
        4. implantes dentales
        5. protesis rodilla
        :  """))
        if nuevo_implante==1:
             medico=int(input("ingrese identificacion del medico responsable: "))
             fecha=input("ingrese fecha:  ")
             estado=input("ingrese estado del implante:")
             cantidad= input("ingrese cantidad:")
             tipofij=input("ingrese tipo de fijacion:")
             tamano=input("ingrese tamaño:")
             material=input("ingrese material:")
             pc=Protesiscadera(medico, fecha, estado,cantidad, tipofij, tamano, material)
             Sistema.nuevo_implante(pc,cedula)
        elif nuevo_implante==2:
             medico=int(input("ingrese identificacion del medico responsable: "))
             fecha=input("ingrese fecha:  ")
             estado=input("ingrese estado del implante:")
             cantidad= input("ingrese cantidad:")
             frec=("ingrese frecuencia de estimulacion: ")
             nelectrodos=("ingrese numero de electrodos: ")
             alambrico=("ingrese si es alambrico o inalambrico: ")
             mp=Marcapasos(medico, fecha, estado, cantidad, frec, nelectrodos, alambrico)
             Sistema.agregarImplante(mp,cedula)
             
        elif nuevo_implante==3:
             medico=int(input("ingrese identificacion del medico responsable: "))
             fecha=input("ingrese fecha:  ")
             estado=input("ingrese estado del implante:")
             cantidad= input("ingrese cantidad:")
             longitud=("ingrese longitud :")
             diametro=("ingrese diametro:")
             material=("ingrese material:")
             s=Stents(medico, fecha, estado, cantidad, longitud, diametro, material)
             Sistema.nuevo_implante(s,cedula)

        elif nuevo_implante==4:
             medico=int(input("ingrese identificacion del medico responsable: "))
             fecha=input("ingrese fecha:  ")
             estado=input("ingrese estado del implante:")
             cantidad= input("ingrese cantidad:")
             forma= input("ingrese forma: ")
             sistfij= input("ingrese sistema de fijacion: ")
             material= input("ingrese material: ")
             id=ImplantesDentales(medico, fecha, estado, cantidad, forma, sistfij, material)
             Sistema.nuevo_implante(id,cedula)

        elif nuevo_implante==5:
             medico=int(input("ingrese identificacion del medico responsable: "))
             fecha=input("ingrese fecha:  ")
             estado=input("ingrese estado del implante:")
             cantidad= input("ingrese cantidad:")
             cedula=int(input("ingrese la cedula del paciente"))
             tipofij=input("ingrese tipo de fijacion:")
             tamano=input("ingrese tamaño:")
             material=input("ingrese material:")
             pr=ProtesisRodilla(medico, fecha, estado, cantidad, cedula, tipofij, tamano, material)
             Sistema.nuevo_implante(pr,cedula)
    
    elif menu==4:
        pass
    elif menu==5:
        break

    else:
        print("ingrese una opcion")