#Se calculara el area de un triangulo a continuacion
#primero se define que la base y la altura son enteros y que la base sera un real, ya que es posible que la division de un numero con decimal
base: int;
altura: int;
resultado: float;
#A continuacion, procedemos a introducir la base y la altura a calcular 
base = int(input("Introduce la base: "));
altura = int(input("Itroduzca la altura: "));
#Y para culminar, se realiza la operacion y se escribe el resultado
resultado = ( base*altura ) / 2;
print("El resultado del area del triangulo serria: ", resultado);