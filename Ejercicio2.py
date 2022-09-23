#Leer información de 10 frutas {nombre, color, precio} para preparar un salpicón;
# el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo+(1)
Salpicon=[]
for i in range(10):
    Fruta={}
    Fruta['nombre']=input('Digite el nombre de la fruta: ')
    Fruta['color']=input('Digite el color de la fruta: ')
    Fruta['precio']=int(input('Digite el precio de la fruta: '))
    Salpicon.append(Fruta)

print(Salpicon)
