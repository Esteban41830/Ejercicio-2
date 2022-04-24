import  csv
class ViajeroFrecuente:
    __NumeroViajero = 0
    __DNI = 0
    __Nombre = ''
    __Apellido = ''
    __MillasAcum = 0.0
    
    def __init__(self, NumeroViajero, DNI, Nombre, Apellido, MillasAcum):
      self.__NumeroViajero = NumeroViajero
      self.__DNI = DNI
      self.__Nombre = Nombre
      self.__Apellido = Apellido
      self.__MillasAcum = float(MillasAcum)

    def cantidadTotalMillas(self):
        return "Millas acumuladas: {}".format(self.__MillasAcum)
    
    def acumularMillas(self,millas):
        self.__MillasAcum = self.__MillasAcum + millas
        return "El nuevo valor es: {}".format(self.__MillasAcum)

    def canjearMillas(self,canje):
        if self.__MillasAcum < canje:
            print("Error, no se puede canjear")
        else:
            print("Se puede canjear\n\nMillas acumuladas: {}".format(self.__MillasAcum))
        
    

if __name__ == '__main__':

    viajeros = []
    archivo = open("viajerofrecuente.csv")
    reader = csv.reader(archivo,delimiter=",")
    
    for fila in reader:
        viajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
        viajeros.append(viajero)

    archivo.close()
        
    num = int(input("Ingrese numero del viajero: \n"))
    print("Ingrese una de las opciones:")
    opcion = ''

    while opcion != "s":
        print("a)_Consultar Cantidad de Millas.\nb)_Acumular Millas.\nc)_Canjear Millas.\ns)_Salir")
        opcion = input()
        
        if opcion == "s":
            break
        
        elif(opcion == "a"):
            print(viajeros[num-1].cantidadTotalMillas())
            print("\nQue operacion desea realizar ahora")
        
        elif(opcion == "b"):
            millas = int(input("Ingrese millas recorridas: "))
            print(viajeros[num-1].acumularMillas(millas))
            print("\nQue operacion desea realizar ahora")
        
        elif(opcion == "c"):
            canje = float(input("Ingrese millas a canjear: "))
            print("\nQue operacion desea realizar ahora")
        
        else:
            print("Ingreso mal la opcion")
            



