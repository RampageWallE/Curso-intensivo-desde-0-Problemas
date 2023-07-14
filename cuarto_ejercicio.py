import requests
opcion = None
while opcion != 0:
    print("[1] Ingresar el lugar ")
    print("[2] Ver la respuesta completa")
    print("[3] Ver la temperatura minima y maxima")
    print("[*] Salir")
    print("NOTA : SI NO INTRODUCE UNA CIUDAD PRIMERO OCURRIRA UN ERROR EN EL PROGRAMA")
    opcion = int(input("\nELIGE UNA DE LA OPCIONES:\t"))
    if opcion == 1:
        lugar = str(input("Ingrese el nombre del lugar:"))
        url = f"https://api.openweathermap.org/data/2.5/weather?q={lugar}&appid=ed1e46cae653fed20553354311e34b1b"
        response = requests.get(url)

    elif opcion == 2:
        if response.status_code == 200:
            print("Se logro conectar con exito")
            respuesta = response.json()
            temp_min = respuesta['main']['temp']
            temp_max = respuesta['main']['temp_max']
            print(f"La temperatura minima en {lugar} es:\t", temp_min)
            print(f"La temperatura maxima en {lugar} es:\t", temp_max)
        else:
            print("No se logro conectar a la API, ingrese un lugar valido")

    elif opcion == 3:
        if response.status_code == 200:
            print("Se logro conectar con exito")
            respuesta = response.json()
            print(respuesta)
        else:
            print("No se logro conectar a la API, ingrese un lugar valido")
    else: 
        break
    