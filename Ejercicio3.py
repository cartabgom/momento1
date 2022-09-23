#Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
#1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.8)
#2. Digitar 2 para mostrar todos los productos registrados (+0.8)
#3. Digitar 0 para SALIR

op=1
productos = []
print("Menú Supermercado")
print("1. Agregar productos al carrito de compras: ")
print("2. Mostrar productos del carrito: ")
print("0. SALIR ")

while(op!=0):
    producto={}
    op=int(input("Ingrese una opción al menú: "))
    if(op==1):
        print("Agregar productos al carrito\n")
        producto['Codigo']=input('Ingrese el codigo del producto: ')
        producto['nombre']=input('Ingrese el nombre del producto: ')
        producto['precio']=input('Ingrese el precio del producto: ')
        productos.append(producto)
    elif(op==2):
        print("Indique los productos registrados en la canasta\n")
        print(productos)
    elif(op==0):
        break
    else:
      print("Seleccione la opcion correcta: ")