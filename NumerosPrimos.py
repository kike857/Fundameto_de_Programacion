#Numeros primos
#Comenzamos definiendo las variables que necesitaremos

num1 = int;
div = int;
cont = int;

#Declaramos nuestras variables
div = 1;
cont = 0;

#Le pedimos al usuario que ingrese el numero que desea revisar si es primo o no lo es
num1 =int(input("Por favor, ingrese un numero: "));

#Usamos el condicional if y elif para los casos especiales, si introduce un numero par distinto a 2 lo descarta (Ya que 2 es el unico numero primo par) y si el usuario introduce un numero menor que 1 nunca sera primo
if num1 == 2:
    print("2 es primo");
elif num1 <= 1:
    print("El numero ", num1, " no es mayor que uno, por lo que no es primo" );

#Si el numero que ingresa el usuario no es ninguno de los anteriores, el algoritmo seguira buscando si el numero es primo a traves de el condicional else
else:
       
    #Comenzamos un ciclo con el divisor (div) empezando en 1, el cual dividira el numero que ingreso el usuario y se asegurara que el residuo de 0, y si eso no pasa se le sumara un 1 al divisor
    while div <= num1:

        #El condicional if le sumara 1 a la variable cont hasta que encuentre un divisor, la variable cont cuenta la cantidad de divisores que posee un numero
        if num1 % div == 0:
            cont = cont + 1;
        div = div + 1;

        #Si nuestra variable cont es mayor a 3, se considera que el numero no es primo y el algoritmo termina el proceso de busqueda con break
        if cont > 3:
            break

        #Aca colocamos una barrera, esta sirve para que los divisores que coloquemos no pasen del limite que coloquemos. Debido a que si colocamos un numero pequenio de barrera el margen de error para los numeros grandes aumenta, ya que no todos los divisores se encuentran entre los primeros 1o digitos
        #Si introducimos un numero grande, lo ideal seria colocar una barrera de divisores alta, para que el margen de error sea mas pequenio
        #Por ejemplo, aca en mi codigo coloque como barrera el numero 150, para que cuando el usuario introduzca un numero grande, este busque entre los divisores del 1 al 1000 para que el proceso sea mucho mas rapido 
        if div >= 1000:
            print("El numero ", num1, " es un numero primo");
            break

    #Si el numero que ingresamos tiene solo dos divisores se toma a el numero como un primo
    if cont == 2:
        print("El numero ", num1, " es un numero primo");

    #Si se da el caso de que el numero que ingrese el usuario tiene mas de tres divisores, automaticamente colocara que no es primo
    if cont >= 3:
        print("El numero ", num1, " no es un numero primo");