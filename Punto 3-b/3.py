#Sin optimizar
L = [1,2,3,4,5,6,7,8,9,11,12]

def operador(Lista):
    P=[]
    for i in Lista:
        j=5+i
        if (j%2==0):
            P.append(i)
    return P
print(operador(L))

# Optimizado
L = [1,2,3,4,5,6,7,8,9,11,12]

def operador1(Lista):
    for i in Lista:
        if (i%2 == 0):
            Lista.remove(i)
    return Lista
print(operador1(L))
















# Primero se inicializa la variable 'L' con una lista que
# contiene los numeros del 1 al 12 en forma ascendente, luego
# se declara la funcion 'operador' y posteriormente es llamada
# dentro de un print pasandole como parametro la lista 'L'.
# Una vez dentro de la funcion  los datos de 'L' se copian a una
# nueva variable llamada 'Lista' y seguido es inicializada la
# variable 'P' con una lista vacia, luego se itera la lista 'Lista'
# con un ciclo for donde a una nueva variable 'j' se le asigna el
# valor que el ciclo tome en determinada iteracion, mas 5, para
# posteriormente comprobar si su valor en ese instante es un numero
# par, de ser ese el caso a la lista 'P' se le agrega el valor que
# tomo el ciclo for de 'Lista' en determinada iteracion. Despues
# de finalizar el ciclo la funcion retorna una lista con los numeros
# impares de la lista que recibio como parametro para luego ser
# imprimida.