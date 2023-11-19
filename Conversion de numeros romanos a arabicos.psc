//Conversion de numeros romanos a arabigos
Proceso NumerosRomanos
    //Comenzamos definiendo nuestras variables
    Definir num_rom como Cadena;
    Definir rom_ind, num_prev, indice, res Como Entero;
	Definir rom_val Como Cadena;
	
    //Aca estamos dandole al programa dos listas simulando un diccionario con todas las opciones posibles
    Dimension rom_ind[7];
    rom_ind[1] <- 1;
    rom_ind[2] <- 5;
    rom_ind[3] <- 10;
    rom_ind[4] <- 50;
    rom_ind[5] <- 100;
    rom_ind[6] <- 500;
    rom_ind[7] <- 1000;
	
	Dimension rom_val[7];
	rom_val[1] <- "I";
	rom_val[2] <- "V";
	rom_val[3] <- "X";
	rom_val[4] <- "L";
	rom_val[5] <- "C";
	rom_val[6] <- "D";
	rom_val[7] <- "M";
	
    res <- 0;   //Empezamos el contador de nuestros enteros en 0
	num_prev <- 0;
	
    //Le pedimos al usuario que introduzca el numero en romano,
    //el programa lo pasara a mayusculas automaticamente con el comando Mayusculas
    Escribir "Introduzca el numero romano que desea convertir: ";
    Leer num_rom;
    num_rom <- Mayusculas(num_rom);
	
    //Comenzamos un bucle for para que el programa pase por cada uno de los numeros romanos que introduzcamos 
    //Por esa misma razon utilizamos el comando len, para que lea cada uno de los numeros romanos que introduzcamos sin saltarlos
	Definir i, j como Entero;
    Para i<-1 Hasta Longitud(num_rom) Hacer
		// Obtenemos el indice con el valor del caracter romano simulando un diccionario
		Para j<-1 Hasta 7 Hacer
			Si Subcadena(num_rom, i, i) = rom_val[j] Entonces
				indice <- j;
			FinSi
		FinPara
		
		//En este if calcularemos el valor de los numeros que introduzamos, (Utilizando la lista que definimos anteriormente)
		//Tambien le estamos dando al programa la forma de calcular los numeros como IV, IX, XL, XC, CD, y CM
		//Si no es uno de los numeros mencionados anteriormente, lo escribira con su valor normal en el else
		Si i > 1 Y indice > 1 Y rom_ind[indice] > num_prev Entonces
			res <- res + rom_ind[indice] - 2 * num_prev;
		SiNo
			res <- res + rom_ind[indice];
		FinSi
		
		num_prev <- rom_ind[indice];
	FinPara
	
	//Mostramos el resultado en pantalla
	Escribir "El numero ", num_rom, " en numeros arabigos seria: ", res;
FinProceso