import datetime

class Implantes:
    def __init__(self, medico, fecha, estado, cantidad, cedula):
        self.__fecha = fecha
        self.__medico = medico
        self.__estado = estado
        self.__cantidad = cantidad
        self.__cedula = cedula
    @property
    def medico(self):
        return self.__medico
    @medico.setter
    def medico(self,medico):
        self.__medico=medico
    @property
    def fecha(self):
        return self.__medico
    @fecha.setter
    def fecha(self,fecha):
        self.__fecha=fecha
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self,estado):
        self.__estado=estado
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad=cantidad
    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula

class Protesiscadera(Implantes):
    def __init__(self,  medico, fecha, estado,cantidad,cedula, tipofij, tamano, material):
        super().__init__( medico, fecha, estado, cantidad, cedula)
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material
    def __str__(self):
        return f"Protesiscadera: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n tipofij:{self.tipofij} \n tamaño:{self.tamano} \n material:{self.material}"
    @property
    def tipofij(self):
        return self.__tipofij
    @tipofij.setter
    def tipofij(self,tipofij):
        self.__tipofij=tipofij
    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self,tamano):
        self.__tamano=tamano
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material=material
class Marcapasos(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad,cedula, frec, nelectrodos, alambrico):
        super().__init__(medico, fecha, estado, cantidad,cedula)
        self.__frec=frec
        self.__nelectrodos=nelectrodos
        self.__alambrico=alambrico

    def __str__(self):
        return f"Marcapasos: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n frecuencia:{self.frec} \n #electrodos:{self.nelectrodos} \n alambrico:{self.alambrico}"
    @property
    def frec(self):
        return self.__frec
    @frec.setter
    def frec(self,frec):
        self.__frec=frec
    @property
    def nelectrodos(self):
        return self.__nelectrodos
    @nelectrodos.setter
    def nelectrodos(self,nelectrodos):
        self.__nelectrodos=nelectrodos
    @property
    def alambrico(self):
        return self.__alambrico
    @alambrico.setter
    def alambrico(self,alambrico):
        self.__alambrico=alambrico
class Stents (Implantes):
    def __init__(self,  medico, fecha, estado, cantidad,cedula, longitud, diametro, material):
        super().__init__(medico, fecha, estado,cantidad,cedula)
        self.__longitud=longitud
        self.__diametro=diametro
        self.__material=material

    def __str__(self):
        return f"Stents: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n longitud:{self.longitud} \n diametro:{self.diametro} \n material:{self.material}"
    @property
    def longitud(self):
        return self.__longitud
    @longitud.setter
    def longitud(self,longitud):
        self.__longitud=longitud
    @property
    def diametro(self):
        return self.__diametro
    @diametro.setter
    def diametro(self,diametro):
        self.__diametro=diametro
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material=material
class ImplantesDentales(Implantes):
    def __init__(self,  medico, fecha, estado, cantidad,cedula, forma, sistfij, material):
        super().__init__(medico, fecha, estado, cantidad,cedula)
        self.__forma=forma
        self.__sistfij=sistfij
        self.__material= material

    def __str__(self):
        return f"Implantes_dentales: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n sistema de fijacion:{self.sistfij} \n forma:{self.forma} \n material:{self.material}"
    @property
    def forma(self):
        return self.__forma
    @forma.setter
    def material(self,forma):
        self.__forma=forma
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material=material
    @property
    def sistfij(self):
        return self.__sistfij
    @sistfij.setter
    def material(self,sistfij):
        self.__sistfij=sistfij
class ProtesisRodilla(Implantes):
    def __init__(self,  medico, fecha,estado, cantidad,cedula, tipofij, tamano, material):
        super().__init__( medico, fecha, estado, cantidad, cedula)
        self.__tipofij=tipofij
        self.__tamano=tamano
        self.__material=material

    def __str__(self):
        return f"ProtesisRodilla: \n medico:{self.medico} \n fecha:{self.fecha} \n estado:{self.estado} \n cantidad:{self.cantidad} \n cedula:{self.cedula} \n tipo de fijacion:{self.tipofij} \n tamaño:{self.tamano} \n material:{self.material}"
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self,material):
        self.__material=material
    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self,tamano):
        self.__tamano=tamano
    @property
    def tipofij(self):
        return self.__tipofij
    @tipofij.setter
    def tipofij(self,tipofij):
        self.__tipofij=tipofij
class Sistema():
    def __init__(self):
        self.implantes=[]
    def agregar_implante(self,implante):
        self.implantes.append(implante)
    def ver_implante(self):
        if not self.implantes:
            print("No hay implantes registrados.")
            return
        for i, implante in enumerate(self.implantes, 1):
            print(f"implante #{i}:")
            print(implante)
            print("-" * 40)
    def actualizar_implante(self, indice, implante_actualizado):
        if indice >= 0 and indice < len(self.implantes):
            self.implantes[indice] = implante_actualizado
            print(f"implante #{indice + 1} actualizada:")
            print(implante_actualizado)
        else:
            print("Índice de implante no válido.")

    def eliminar_implante(self, indice):
        if indice >= 0 and indice < len(self.implantes):
            implante_eliminado = self.implantes.pop(indice)
            print(f"Implante #{indice + 1} eliminado:")
            print(implante_eliminado)
        else:
            print("Índice de implante no válido.")
sistema = Sistema()
while True:
    menu = int(input("""ingrese la opcion que dese seleccionar:
    1. Ingresar un nuevo implante
    2. Eliminar implante
    3. Editar información del implante 
    4. Visualizar el inventario completo
    5. Salir del sistema
    """))

    if menu == 1:
        tipoimp = int(input("""ingrese el implante a ingresar:
        1. protesis cadera
        2. marcapasos
        3. stents
        4. implantes dentales
        5. protesis rodilla
        :  """))
        if tipoimp == 1:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante: ")
            cantidad = input("ingrese cantidad: ")
            cedula = int(input("ingrese la cedula del paciente: "))
            tipofij = input("ingrese tipo de fijacion:")
            tamano = input("ingrese tamaño:")
            material = input("ingrese material:")
            pc = Protesiscadera(medico, fecha, estado, cantidad, cedula, tipofij, tamano, material)
            sistema.agregar_implante(pc)

        elif tipoimp == 2:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = int(input("ingrese la cedula del paciente"))
            frec = input("ingrese frecuencia de estimulacion: ")
            nelectrodos = input("ingrese numero de electrodos: ")
            alambrico = input("ingrese si es alambrico o inalambrico: ")
            mp = Marcapasos(medico, fecha, estado, cantidad, cedula, frec, nelectrodos, alambrico)
            sistema.agregar_implante(mp)

        elif tipoimp == 3:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = int(input("ingrese la cedula del paciente"))
            longitud = input("ingrese longitud :")
            diametro = input("ingrese diametro:")
            material = input("ingrese material:")
            s = Stents(medico, fecha, estado, cantidad, cedula, longitud, diametro, material)
            sistema.agregar_implante(s)
        elif tipoimp == 4:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = int(input("ingrese la cedula del paciente"))
            forma = input("ingrese forma: ")
            sistfij = input("ingrese sistema de fijacion: ")
            material = input("ingrese material: ")
            id = ImplantesDentales(medico, fecha, estado, cantidad, cedula, forma, sistfij, material)
            sistema.agregar_implante(id)
        elif tipoimp == 5:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = int(input("ingrese la cedula del paciente"))
            tipofij = input("ingrese tipo de fijacion:")
            tamano = input("ingrese tamaño:")
            material = input("ingrese material:")
            pr = ProtesisRodilla(medico, fecha, estado, cantidad, cedula, tipofij, tamano, material)
            sistema.agregar_implante(pr)
        else:
            continue
    elif menu == 2:
        ti = int(input("ingrese indice de implante a eliminar tomando el cero como posición 1: "))
        sistema.eliminar_implante(ti)
    elif menu == 3:
        indice=int(input("ingrese indice de implante a modificar tomando el cero como posición 1: "))
        nuevo_implante = int(input("""ingrese el implante a ingresar:
        1. protesis cadera
        2. marcapasos
        3. stents
        4. implantes dentales
        5. protesis rodilla
        :  """))
        if nuevo_implante == 1:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = input('ingrese la cedula del paciente')
            tipofij = input("ingrese tipo de fijacion:")
            tamano = input("ingrese tamaño:")
            material = input("ingrese material:")
            pc = Protesiscadera(medico, fecha, estado, cantidad,cedula, tipofij, tamano, material)
            sistema.actualizar_implante(indice,pc )
        elif nuevo_implante == 2:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = input('ingrese la cedula del paciente')
            frec = input("ingrese frecuencia de estimulacion: ")
            nelectrodos = input("ingrese numero de electrodos: ")
            alambrico = input("ingrese si es alambrico o inalambrico: ")
            mp = Marcapasos(medico, fecha, estado, cantidad, cedula, frec, nelectrodos, alambrico)
            sistema.actualizar_implante(indice,mp )

        elif nuevo_implante == 3:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = input('ingrese la cedula del paciente')
            longitud = input("ingrese longitud :")
            diametro = input("ingrese diametro:")
            material = input("ingrese material:")
            s = Stents(medico, fecha, estado, cantidad, cedula, longitud, diametro, material)
            sistema.actualizar_implante(indice,s)

        elif nuevo_implante == 4:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = input('ingrese la cedula del paciente')
            forma = input("ingrese forma: ")
            sistfij = input("ingrese sistema de fijacion: ")
            material = input("ingrese material: ")
            id = ImplantesDentales(medico, fecha, estado, cantidad,cedula, forma, sistfij, material)
            sistema.actualizar_implante(indice,id)

        elif nuevo_implante == 5:
            medico = int(input("ingrese identificacion del medico responsable: "))
            año=int(input("ingrese el año: "))
            mes=int(input("ingrese el mes"))
            dia=int(input("ingrese el dia"))
            fecha = datetime.datetime(año, mes, dia)
            estado = input("ingrese estado del implante:")
            cantidad = input("ingrese cantidad:")
            cedula = int(input("ingrese la cedula del paciente"))
            tipofij = input("ingrese tipo de fijacion:")
            tamano = input("ingrese tamaño:")
            material = input("ingrese material:")
            pr = ProtesisRodilla(medico, fecha, estado, cantidad, cedula, tipofij, tamano, material)
            sistema.actualizar_implante(indice,pr)

    elif menu == 4:
        sistema.ver_implante()
    elif menu == 5:
        break

    else:
        print("ingrese una opcion")