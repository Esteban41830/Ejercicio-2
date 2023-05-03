import csv
class ViajeroFrecuente:
	__num_viajero = 0
	__dni = ''
	__nombre = ''
	__apellido = ''
	__millas_acum = 0.0


	def __init__(self, num_viajero,dni,nombre,apellido, millas):
		self.__num_viajero = num_viajero
		self.__dni = dni
		self.__nombre = nombre
		self.__apellido = apellido
		self.__millas_acum = millas
        

	def cantidadTotalMillas(self):
		return self.__millas_acum
    
	def numero(self):
		return self.__num_viajero


	def acumularMillas(self,nuevas_millas):
		self.__millas_acum = self.__millas_acum + nuevas_millas
		

	def canjearMillas(self,canje):
		if self.____millas_acum >= canje:
			self.__millas_acum = self.__millas_acum - canje
		else:
			print('No ha recorrido suficientes millas para canjear')


		return self.__millas_acum



if __name__ == '__main__':
    
    viajeros = []
    archivo = open('ViajeroFrecuente.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        unViajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
        viajeros.append(unViajero)
    
    archivo.close()
    
    print('-------Ingrese una opcion-------\n')
    opcion = ''
    while opcion != 's':
        opcion = input('a-Consultar Cantidad de Millas.\nb-Acumular Millas.\nc-Canjear Millas.\ns-.Salir.\n')
        
        if opcion == 'a':
            num = input('Ingrese el numero del viajero: ')
            i = 0
            ban = False
            while ban == False:
                if viajeros[i].numero() == num:
                    ban = True
                else:
                    i = i+1
            
            print('La cantidad total es de: {}'.format(viajeros[i].cantidadTotalMillas()))
            print('\n¿Que de desea hacer ahora?\n')
        
        elif opcion == 'b':
            num = input('Ingrese el numero del viajero: ')
            i = 0
            ban = False
            while ban == False:
                if viajeros[i].numero() == num:
                    ban = True
                else:
                    i = i+1
                    
            nuevas_millas = float(input('Ingrese las millas recorridas: '))
            viajeros[i].acumularMillas(nuevas_millas)
            print('Valor de millas actualizado: {}'.format(viajeros[i].cantidadTotalMillas()))
            print('\n¿Que desea hacer ahora?\n')
        
        elif opcion == 'c':
            num = input('Ingrese el numero del viajero: ')
            i = 0
            ban = False
            while ban == False:
                if viajeros[i].numero() == num:
                    ban = True
                else:
                    i = i+1
                    
            canje = float(input('Ingrese las millas a canjear: '))
            viajeros[i].canjearMillas(canje)
            print('Valor de millas actualizado: {}'.format(viajeros[i].cantidadTotalMillas()))
            print('\n¿Que desea hacer ahora?\n')
        
        elif opcion == 's':
            print('\n\n-----------FIN DEL PROGRAMA-----------')
        
        else:
            print('Ingreso mal la opcion')
            
        
        

