# Diccionarios de productos y stock de la tienda de DAGOpc 
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = sum(stock[modelo][1] for modelo in productos if productos[modelo][0].lower() == marca)
    print(f"El stock es: {total_stock}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if cantidad > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    
    if resultados:
        resultados.sort()
        print(f"Los notebooks entre los precios consultas son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False

def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        opcion = input("Ingrese opción: ")
        
        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)
        
        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                if modelo in stock:
                    break
                else:
                    print("El modelo no existe!!")
            while True:
                try:
                    precio_nuevo = int(input("Ingrese precio nuevo: "))
                    break
                except ValueError:
                    print("Debe ingresar un valor entero para el precio.")
            if actualizar_precio(modelo, precio_nuevo):
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
            
            while True:
                continuar = input("Desea actualizar otro precio (s/n)?: ").lower()
                if continuar in ['s', 'n']:
                    break
            if continuar == 'n':
                continue
        
        elif opcion == '4':
            print("Programa finalizado.")
            break
        
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    print("Bienvenido al sistema de gestión de notebooks.")
    print("Desarrollado por Dagoberto Pérez")
    main()
