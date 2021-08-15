# Universidad de antioquia
# Bioingenieria
# Valeria Giraldo Agudelo

import random
import time

def clearScreen():
    # Esta funcion imprime un salto de line 30 vecez, dando 
    # la ilucion de limpiar la consola
    print("\n"*30)
        
def imprimir(__sancadas__, etapa, __competidores__):
    # Esta funcion es la encargada de imprimir la carrera en consola
    pista = "Start_|" + "_"*60 + "|_Finish" # Esto es la pista en forma de strings
    
    clearScreen()
    print("~"*((75-len(etapa))//2) + etapa + "~"*((75-len(etapa))//2)) # Aqui se impime la cabezera de la carrera
    for i in range(0,len(__competidores__)):
        print(pista[:__sancadas__[i]] + str(__competidores__[i]) + pista[__sancadas__[i]+1:])


sancadas = [5]*4 # Esta lista almacenara las sancadas que daran los caballos en la pista
ganadores = []  # Esta lista almacenara los dos ganadores de la semifinal

imprimir(sancadas, " SEMIFINAL ",[1,2,3,4]) # Se imprimen los caballos detras de la linea de salida
while len(ganadores) < 2: 
    for j in range(0,len(sancadas)):
        sancadas[j] = sancadas[j] + random.randint(1, 2) # Se genera un numero aleatoreo para la nueva sancada de un caballo
        if sancadas[j] >= 68: # Si la sancada generada anteriormente pasa la lina de meta se posiona el caballo detras de esta(en pantalla)
            sancadas[j] = 68
            if len(ganadores)==0 or (j+1!=ganadores[0] and len(ganadores)<2): # Se verifica que no halla mas de dos ganadores
                ganadores.append(j+1) # Se añade el caballo que halla ganado o quedado de segundo a la lista 'ganadores'
    
    imprimir(sancadas, " SEMIFINAL ",[1,2,3,4]) # Se imprimen en pantalla las sancadas generadas anteriormente
    time.sleep(0.4) # Se detiene el tiempo 4 milisegundos para una mejor visualizacion de la carrera

print("\nClasifican:", ganadores[0], "y", ganadores[1]) # Se muestran en pantalla los dos caballos clasificados a la final
input("Presione enter para pasar a la final: ")

sancadas = [5]*2 # Ahora 'sancada' solo almacenara las sancandas de los dos caballos clsificados
ganadores.sort() # Se organizan de forma ascendente los caballos clasificados
ganador = ganadores[:] # Se crea una copia de los clasificados para posteriormente eliminir al caballo que cruce primero la meta

imprimir(sancadas, " FINAL ", ganadores) # Se imprimen los caballos detras de la linea de salida
while len(ganador)>1:
    for j in range(0, len(sancadas)):
        sancadas[j] = sancadas[j] + random.randint(1, 2) # Se genera un numero aleatoreo para la nueva sancada de un cabballo
        if sancadas[j] >= 68: # Si la sancada generada anteriormente pasa la lina de meta se posiona el caballo detras de esta(en pantalla)
            sancadas[j] = 68
            ganador.pop(j) # Se elimina de la lista de clasificados el caballo que cruzo primero la meta
      
    imprimir(sancadas, " FINAL ", ganadores) # Se imprimen en pantalla las sancadas generadas anteriormente
    time.sleep(0.4) # Se detiene el tiempo 4 milisegundos para una mejor visualizacion de la carrera
        
print("\nEl ganador es:", ganador[0]) # Se muestra en pantalla el caballo ganador
        
        
        