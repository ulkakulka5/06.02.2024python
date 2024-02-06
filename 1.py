def min(lista,rozmiar):#zwraca indeks najmniejszej
    najm=lista[0]
    inx=0

    while rozmiar>0:
        if lista[rozmiar-1]<lista[rozmiar-2]:
            najm=lista[rozmiar-1]
            inx=rozmiar-1
        rozmiar=rozmiar-rozmiar
    return inx

def bubble(lista,rozmiar):
    n=rozmiar
    while n>0:
        for i in range (0,(rozmiar-1)):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1 ]=lista[i+1], lista[i]
            
        n=n-1

    return lista


x=[12,123,1235,8,0,-7]
print(min(x,6))
print(bubble(x,6))
    
