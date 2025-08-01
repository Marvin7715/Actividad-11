propietarios = {}

print(".........Control de vehículos.........")
cantidad = int(input("¿Cuántos propietarios desea registrar?: "))

for i in range(cantidad):
    print(f"\nPropietario #{i + 1}:")
    while True:
        nit = input("Identificación (NIT): ").strip()
        if nit in propietarios:
            print("Este NIT ya existe. Ingrese uno diferente.")
        else:
            break
    nombre = input("Nombre completo: ").strip()
    telefono = input("Teléfono: ").strip()
    cantidad_vehiculos = int(input("Cantidad de vehículos: "))

    vehiculos = {}
    for j in range(cantidad_vehiculos):
        print(f"\nVehículo #{j + 1}:")
        while True:
            placa = input("Placa: ").strip().upper()
            if placa in vehiculos:
                print("Esta placa ya fue ingresada para este propietario.")
            else:
                break
        marca = input("Marca: ").strip().upper()
        modelo = input("Modelo: ").strip().upper()
        anio = int(input("Año: "))
        impuesto = input("¿Pagó el impuesto? (Sí/No): ").strip().lower()
        impuesto_pagado = "Sí" if impuesto in ("sí", "si", "s") else "No"

        vehiculos[placa] = {
            "marca": marca,
            "modelo": modelo,
            "año": anio,
            "impuesto_pagado": impuesto_pagado
        }

    propietarios[nit] = {
        "nombre": nombre,
        "telefono": telefono,
        "vehiculos": vehiculos
    }

print("\nResumen de propietarios:")
total_pagados = 0
total_no_pagados = 0
for nit, datos in propietarios.items():
    print(f"\nIdentificación: {nit}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Teléfono: {datos['telefono']}")
    print("Vehículos:")
    for placa, v in datos["vehiculos"].items():
        print(f"  - Placa: {placa} | {v['marca']} {v['modelo']} ({v['año']}) | Impuesto: {v['impuesto_pagado']}")
        if v["impuesto_pagado"] == "Sí":
            total_pagados += 1
        else:
            total_no_pagados += 1

print(f"\nTotal de vehículos con impuesto pagado: {total_pagados}")
print(f"Total de vehículos sin pagar: {total_no_pagados}")