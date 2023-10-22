Proceso NumerosPrimos
	
//Comenzamos definiendo las variables que necesitaremos
Definir num1, div, cont como entero
	
//Declaramos nuestras variables
div = 1
cont = 0

//Le pedimos al usuario que ingrese el numero que desea revisar si es primo o no lo es
Escribir Sin Saltar "Por favor ingrese el n�mero que desea calcular: "
Leer num1

//#Usamos el condicional si y sino para los casos especiales, si introduce un numero par distinto a 2 lo descarta (Ya que 2 es el unico numero primo par) y si el usuario introduce un numero menor que 1 nunca sera primo
Si num1 == 2 Entonces
	Escribir "El numero 2 es un numero primo"
Sino
	Si num1 <= 1 Entonces;
		Escribir "El numero ", num1, " No es mayor a 1, por lo que no es un numero primo"
	SiNo
		
		//Si el numero que ingresa el usuario no es ninguno de los anteriores, el algoritmo seguira buscando si el numero es primo a traves de el condicional Mientras 
		//Comenzamos un ciclo con el divisor (div) empezando en 1, el cual dividira el numero que ingreso el usuario y se asegurara que el residuo de 0, y si eso no pasa se le sumara un 1 al divisor
		Mientras div <= num1 Hacer
			
			
			//El condicional si le sumara 1 a la variable cont hasta que encuentre un divisor, la variable cont cuenta la cantidad de divisores que posee un numero
			Si num1 % div == 0 Entonces;
                cont = cont + 1
			Fin Si
			div = div + 1
			
			// Si nuestra variable cont es mayor a 3, se considera que el numero no es primo y el algoritmo termina el proceso de busqueda con el FinSi
			Si cont > 3 Entonces;
			Fin Si
			
			//Aca colocamos una barrera, esta sirve para que los divisores que coloquemos no pasen del limite que coloquemos. Debido a que si colocamos un numero pequenio de barrera el margen de error para los numeros grandes aumenta, ya que no todos los divisores se encuentran entre los primeros 1o digitos
			//Si introducimos un numero grande, lo ideal seria colocar una barrera de divisores alta, para que el margen de error sea mas pequenio
			//Por ejemplo, aca en mi codigo colocamos como barrera el numero 1000, para que cuando el usuario introduzca un numero grande, este busque entre los divisores del 1 al 1000 para que el proceso sea mucho mas rapido
			Si div >= 1000 Entonces
				Escribir "El numero ", num1, " es un numero primo "
			FinSi
		FinMientras
		
			// Si el numero que ingresamos tiene solo dos divisores se toma a el numero como un primo
			Si cont == 2 Entonces;
				Escribir "El n�mero ", num1, " es un numero primo";
			Finsi
			
			//Si se da el caso de que el numero que ingrese el usuario tiene mas de tres divisores, automaticamente colocara que no es primo
			Si cont >= 3 Entonces;
				Escribir "El n�mero ", num1, " no es un numero primo "
			Fin Si
		FinSi
	Finsi

//Terminamos nuestro Proceso 
FinProceso