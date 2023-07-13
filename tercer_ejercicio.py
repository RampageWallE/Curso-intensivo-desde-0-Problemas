def funcion(N):
    lista2=[]
    for x in range(1, N+1):
        lista=[]
        for y in range(1, x+1):
            if x%y==0: 
                lista.append(y)
        if len(lista) in [1,2]:
            lista2.append(x)
    print(lista2)
funcion(5)
            

# que se debe de hacer?
#     hallar multiplos, osea que el residuo sea 0 
# que es lo que quiero?
#     Una ves dividido quiero comprobar que el numero tengo solo 2 divisores 


