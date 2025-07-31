propietarios = {}

print(".........Control de vehículos.........")
cantidad = int(input("¿Cuántos propietarios desea ingresar?: "))

for i in range(cantidad):
    print(f"\nUsuario #{i + 1}:")

    while True:
        nit = input("Número de identificación (NIT) (ej. 1234567890101): ").strip()
        if nit in propietarios:
            print("Este nit ya existe. Ingrese un nit diferente.")
        else:
            break

    nombre_completo = input("Nombre completo del propietario: ").strip()
    telefono = int(input("¿Cuál es el numero de telefono del propietario?: "))

    propietarios[nit] = {
        "nombre": nombre_completo,
        "telefono": telefono
    }

    vehiculos = {}

    cantidad_vehiculos = int(input("Ingrese la cantidad de vehículos que posee el propietario: "))

    placa = input("Ingrese el numero de placa del vehiculo: ").strip().upper()
    marca = input("Ingrese la marca del vehiculo: ").strip().upper()
    modelo = input("Ingrese el modelo del vehiculo: ").strip()
    anio = int(input("Ingrese el año de fabricación del vehiculo: "))
    estado_del_impuesto =input("¿El impuesto del vehículo esta pagado? (SI/NO): ")

    propietarios [placa] ={
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "impuesto": estado_del_impuesto
}

print("\nLista de propietarios registrados:")
for nit, datos in propietarios.items():
    print(f"\nNúmero de Identificacíon: {nit}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Telefono: {datos['telefono']}")
for placa, datos in propietarios.items():
    print(f"Número de placa: {datos['placa']}")
    print(f"Marca del vehiculo: {datos['marca']}")
    print(f"Año del vehiculo: {datos['anio']}")
    print(f"Impuesto pagado: {datos['impuesto']}")