diccionario:dict={}
diccionario.setdefault(0,{"nombre":"Piero","telefono":962483840})
diccionario.setdefault(2,{"nombre":"Genesis","telefono":96248384})
diccionario.setdefault(1,{"nombre":"Kenny","telefono":96248384})
diccionario.setdefault(3,{"nombre":"Ken","telefono":96248384})
diccionario.setdefault(4,{"nombre":"Leonor","telefono":96248384})
diccionario.setdefault(5,{"nombre":"Genara","telefono":96248384})
opcion=None
while opcion !=0:

    print("""
    [1] Ingresar un nuevo registro
    [2] Buscar registros por nombres   
    [3] Mostrar todos los registros   
    [0] Cerrar programa      
          """)
    
    opcion=int(input("  ingrese la opcion que desee:\t"))  
    if opcion==1:
        print("INGRESE EL NOMBRE Y NUMERO DE CELULAR DE LA PERSONA")
        nombre=str(input("NOMBRE DE LA PERSONA:\t"))
        telefono=int(input("CELULAR DE LA PERSONA:\t"))
        contador = max(diccionario.keys()) + 1
        diccionario.setdefault(contador,{"nombre":nombre, "telefono":telefono})
        print("#EL REGISTRO FUE AÑADIDO")
        pass    

    elif opcion==2:
        cadena= str(input("Ingrese el caracter a buscar:\t"))
        print("El resultado de su busqueda fue: ")
        for i in diccionario.values():
            if(i.get("nombre").find(cadena)>=0):
                print("- ", i)
    elif opcion==3:
        print("Todos los registros son los siguientes:")
        for i,b in diccionario.items():
            print(i, b)
    elif opcion==0:
        break
    else:
        print(" INGRESE UNA OPCION VALIDA")