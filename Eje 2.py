import  csv
class ViajeroFrecuente:
    def __init__(self, numero_viajero, dni, nombre, apellido, millas_acum):
      self.__numero_viajero = numero_viajero
      self.__dni = dni
      self.__nombre = nombre
      self.__apellido = apellido
      self.__millas_acum = millas_acum

    def cantidadTotalMillas(self):
        return "Millas acumuladas:",self.__millas_acum

    def acumularMillas(self,millas):
        self.__millas_acum = self.__millas_acum + millas
        return "El nuevo valor es: ",self.__millas_acum

    def canjearMillas(self,canje):
        if self.__millas_acum <= canje:
            print("Error, no se puede canjear")
        
        return "Se puede canjear, millas acumuladas: ",self.__millas_acum
    

if __name__ == '__main__':

    viajeros = []
    with open("viajerofrecuente") as archivo:
        reader = csv.reader(archivo,delimiter=';')
        
        for fila in reader:
            viajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
            viajeros.append(viajero)

        archivo.close()
        
    opcion = ""
    while opcion != "s":
        print("Ingrese una de las opciones:\n")
        opcion = (input("a) Consultar Cantidad de Millas.\nb) Acumular Millas.\nc) Canjear Millas.\ns) Salir"))
        if opcion == "s":
            break
        elif(opcion == "a"):
            num = int(input("Ingrese numero del viajero: "))
            print(viajeros[num-1].cantidadTotalMillas());break
        elif(opcion == "b"):
            num = int(input("Ingrese numero del viajero: "))
            millas = int(input("Ingrese millas recorridas: "))
            print(viajeros[num-1].acumularMillas(millas));break
        elif(opcion == "c"):
            num = int(input("Ingrese numero del viajero: "))
            canje = int(input("Ingrese millas recorridas: "))
            print(viajeros[num-1].canjearMillas(canje));break
        else:
            print("Ingreso mal la opcion")



