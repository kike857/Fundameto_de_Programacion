# Conversión de numeros romanos a arabicos
# Comenzamos definiendo nuestras variables

num_rom: str
rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} # Aca estamos dandole al programa un diccionario con todas las opciones posibles
ent = 0 # Empezamos el contador de nuestros enteros en 0

# Le pedimos al usuario que introduzca el numero en romano, el programa lo pasara a mayusculas automaticamente con el comando .upper()
num_rom = str(input("Introduzca el numero romano que desea convertir: ")).upper ( )

#Comenzamos un bucle for para que el programa pase por cada uno de los numeros romanos que introduzcamos 
#Por esa misma razon utilizamos el comando len, para que lea cada uno de los numeros romanos que introduzcamos sin saltarlos
for i in range(len(num_rom)):
    
    #En este if calcularemos el valor de los numeros que introduzamos, (Utilizando el diccionario que definimos anteriormente)
    #Tambien le estamos dando al programa la forma de calcular los numeros como IV, IX, XL, XC, CD, y CM
    #Si no es uno de los numeros mencionados anteriormente, lo escribira con su valor normal en el else
    if i > 0 and rom[num_rom[i]] > rom[num_rom[i - 1]]:
        ent += rom[num_rom[i]] - 2 * rom[num_rom[i - 1]]
    else:
        ent += rom[num_rom[i]]

#Mostramos el resultado en pantalla
print ("El numero ", num_rom, "En numeros arabicos seria: ", ent)