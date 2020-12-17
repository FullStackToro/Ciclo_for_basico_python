#1.- Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "grande".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def tamañoGrande(lista):
    print('\n 1.- Función tamaño grande:')
    for x in range (0,len(lista),1):
        if lista[x]>0:
            lista[x]='Grande'
    print('La lista modificada es:', lista)
#2.-Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos.
# (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def contarPositivos(lista):
    print('\n 2.- Función contar positivos:')
    count=0
    for x in range (0, len(lista),1):
        if lista[x]>0:
            count=count+1
    lista.pop
    lista.append(count)
    print('La nueva lista es:',lista)

#3.-Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sumaTotal(lista):
    print('\n 3.- Función suma total:')
    sum=0
    for x in range (0, len(lista),1):
        sum=lista[x]+sum
    print('La suma total de la lista',lista, 'es:',sum)


#4.-Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def avg(lista):
    print('\n 4.- Función promedio:')
    sum=0
    for x in range (0, len(lista),1):
        sum=lista[x]+sum
    print('El promedio de la lista',lista, 'es:',sum/len(lista))


#5.-Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
def longitud(lista):
    print('\n 5.- Función longitud:')
    print('La longitud de la',lista, 'es:',len(lista))

#6.-Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False

def minimo(lista):
    print('\n 6.- Función mínimo:')
    if len(lista)==0:
        print(False)
        return
    else:
        min=lista[0]
        for x in range(0,len(lista),1):
            if lista[x]<min:
                min=lista[x]
    print('El mínimo de la lista', lista, 'es:',min)

#7.-Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False

def maximo(lista):
    print('\n 7.- Función máximo:')
    if len(lista)==0:
        print(False)
        return
    else:
        max=lista[0]
        for x in range(0,len(lista),1):
            if lista[x]>max:
                max=lista[x]
    print('El máximo de la lista', lista, 'es:',max)

#8.-Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

def analisisFinal(lista):
    print('\n 8.- Función analisis final:')
    if len(lista)==0:
        print(False)
        return
    else:
        min=lista[0]
        max = lista[0]
        sum=0
        for x in range(0,len(lista),1):
            sum=lista[x]+sum
            if lista[x]<min:
                min=lista[x]
            elif lista[x] > max:
                max = lista[x]
        diccionario={'Total':sum,'Promedio':sum/len(lista),'Mínimo':min,'Máximo':max,'Longitud': len(lista)}
        print('El diccionario es:',diccionario)





#9.-Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def inversa(lista):
    print('\n 9.- Función inversa:')
    var=len(lista)/2
    var=int(var)
    for x in range(0, var, 1):
        temp=lista[x]
        lista[x]=lista[var*2-1-x]
        lista[var*2-1-x]=temp
    print('La lista inversa es:',lista)



if __name__ == '__main__':

    tamañoGrande([- 1, 3, 5, -5])
    contarPositivos([-1,1,1,1])
    contarPositivos([1, 6, -4, -2, -7, -2])
    sumaTotal([1, 2, 3, 4])
    sumaTotal([6, 3, -2])
    avg([1, 2, 3, 4])
    longitud(([37,2,1, -9]))
    minimo([37, 2, 1, -9])
    maximo([37, 2, 1, -9])
    analisisFinal([37, 2, 1, -9])
    inversa([37, 2, 1, -9])

