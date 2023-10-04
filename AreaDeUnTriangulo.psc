//Se calculara el area de un triangulo
Algoritmo AreaDeUnTriangulo
	//Primero se definira la base y altura como entero
	Definir base, altura Como Entero;
	//Se prosigue introduciendo los numeros a calcular
	Escribir "Introduzca la base";
	Leer base;
	Escribir "Ahora introduzca la altura";
	Leer altura;
	//Ahora, se introduce que el resultado se define como un real debido a que la division puede dar un numero decimal
	Definir resultado Como Real;
	Escribir "Su resultado es";
	//Por ultimo, se calcula el resultado de la operacion dividiendo la base por la altura entre dos y se escribe el resultado 
	resultado <- ((base + altura) / 2);
	Escribir resultado;
FinAlgoritmo