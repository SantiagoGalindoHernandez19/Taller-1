# Taller-1

1) Realizacion quiz Python Beginner
![QUIZ](https://user-images.githubusercontent.com/124641609/224518688-a9d098e3-bd8e-408a-8e64-dcf4996af3f2.JPG)

---

2)Realice un programa que lea tres números reales y determine cuál es el mayor.

Solucion
1. Iniciamos definiendo la varibale con ayuda de la funcion input dentro de la funcion int, donde se reflejara un mensaje para que el usuario digite los 3 numeros a escoger

![Captura 2](https://user-images.githubusercontent.com/124641609/224518958-4b68a63f-dfb9-4d19-b1b6-837aad3eb51f.JPG)

2. Para no tener ningu inconveniente respecto a que los numeros sean los mismos , utilizamos el condicional if , de modo que la variable x,y,z sean diferentes.Asimismo acompañaremos esta condicion con una parte falsa  para que el usuario vuelva a digitar otro numero diferente 

![Captura](https://user-images.githubusercontent.com/124641609/224519409-031069df-c580-496d-a956-44ae853e9c35.JPG)

3. Por ultimo  impondremos un par de condiciones utilizando el mayor que, con sus partes falsas de tal modo que el programa determine cual de los 3 numeros sera el mayor 

![Captura3](https://user-images.githubusercontent.com/124641609/224519566-0d36b824-0ab9-4d52-8d7b-c8ec5753584c.JPG)

---

3)Realice un programa que lea un número entero y determine si es par o impar.

1.Empezamos definiendo la variable x  dentro de la funcion int para la digitacion del numero, de este modo establecemos una division del numero digitado entre 2 haciendo uso del % puesto que este se utiliza para el resudio de aquella division, al ser 0 esta decimos que el numero es par

![Captura4](https://user-images.githubusercontent.com/124641609/224519878-464108b4-a6c9-4007-b228-daf75b134d8b.JPG)

2.Posteriormente escribiremos una parte falsa, la cual representara el numero impar 


![Captura 4](https://user-images.githubusercontent.com/124641609/224520078-283b17da-f3a9-4b1f-9419-261838e8a962.JPG)

---

4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

1.  Primero definimos la funcion con ayuda de la condicional if , pues con esto decimos que si el residuo entre la division del primer numero con el segundo da como residuo 0, es multiplo

![Captura 5](https://user-images.githubusercontent.com/124641609/224526839-8f2d06cd-2aa1-4aab-9263-90d2e619c703.JPG)

2.De este modo agregamos la partefalsa en caso de que no sea multiplo y por ultimo definimos las variables para digitar 

![Captura8](https://user-images.githubusercontent.com/124641609/224526909-e1f8f63d-f807-44b7-8208-662a8770cbac.JPG)

---

5)Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

1.Asignaremos 3 variables para la correcta digitacion numerica

![WhatsApp Image 2023-03-12 at 1 00 45 AM](https://user-images.githubusercontent.com/124641609/224527244-247b0588-8016-4b80-9d9a-ca5fb555034d.jpeg)

2. Haciendo uso el condicional if, imponemos 3 casos que puedan llegar a suceder, si es mayor, menor o igual que la suma de los dos primeros numeros

![Captura11](https://user-images.githubusercontent.com/124641609/224527890-77e7aa08-22a0-4bab-aff4-435e673d9399.JPG)

---

6) Escriba un programa que solicite al usuario una letra y determine si es una voz o una consonante.
1. Se define la variable vocales, con una cadena de valores, debemos tener en cuenta que deben aparecer tanto en mayusculas como minusculas .Con ayuda del condicional if estipulamos que si el usuario digita algun valor de la lista sera una vocal, de lo contraria sera una consonante y por ultimo validamos.



![WhatsApp Image 2023-03-12 at 1 28 17 AM](https://user-images.githubusercontent.com/124641609/224562603-02b36dc2-403c-4b36-8f9f-ef30e65beec0.jpeg)

---

7)Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

El promedio:

a. Definimos la 5 variables a usar con ayuda de la funcion int(input), luego llamaremos a la variable prom al procedimiento de sumar los 5 valores entre la cantidad de caracteres, de esta manera lo unico que faltaria seria  imprimir la respuesta.

![CAPTURA PROMEDIO](https://user-images.githubusercontent.com/124641609/224568878-35b3b415-1eef-42d5-b453-689fec764cc0.JPG)

La mediana:

b.Basicamente para este prodecimiento se hizo uso de una cadena, para poder estipular mas facil los valores, principalmente se debia leer esta misma cadena para al momento de que fuera leida, organizara del mismo modo los valores, con ayuda de la funcion half y len, haremos que las lecturas sean cada vez menores

![MEDIANA](https://user-images.githubusercontent.com/124641609/224569193-563aecce-42af-4f8e-9dea-80547c1b0f39.JPG)

El promedio  multiplicativo:

c. Asignamos una variable para la multiplicacion de los 5 numeros, siguiente a eso hacemos uso de la funcion predeterminada para sacar la raiz sqrt pues de este modo se facilita el manejo del resultado

![Promedio multiplicativo](https://user-images.githubusercontent.com/124641609/224571469-4d637106-ccf9-40d9-bd45-1f2dc3a6e1db.JPG)

Ordenar los números de forma ascendente:

d. El procedimiento realizado en este paso es similar al de la mediana ya que hacemos uso de 3 funciones importantes a la lectura de las cadenas las cuales son range, temp posicion. Lo que hicimos aqui fue basicamente que el programa leyera primero los 5 numeros y determinara si es mayor uno que el otro, despues que lo lea 4 veces, y despues 3 veces asi hasta que llegue a 1.Ordenar los numeros de forma descendente

![Orden lista arriba](https://user-images.githubusercontent.com/124641609/224571730-cb9c9e9b-9be3-46c9-8eaa-eeb82af273d9.JPG)

Ordenar los numeros de forma descendente:

Hacemos el mismo procedimiento pero en vez de que la lectura de numeros sea mayor modificamosel signo para que sea menor 

![Orden lista ABAJO](https://user-images.githubusercontent.com/124641609/224571903-9a0f267c-973c-4168-bad9-0e980361b375.JPG)

La potencia del mayor número elevado al menor número

F. Creamos un programa que nos de el valor del numero mayor  y el n umero menor de la lis ta, de esta manera nos queda mas facil porque podemos operar los resultados que dan
independientemente de la modificacion de los numeros 

![POTENCIA](https://user-images.githubusercontent.com/124641609/224572182-32cd5039-e1ca-455d-9e62-81a4675be080.JPG)

La raíz cúbica del menor número

g. Con el procedimiento anteriormente realiado solo queda seleccionar y operar el numero menor con las siguientes instruciones (**(1/3)) que seria el procedimiento 
sacar la raiz cubica

![Raiz cubica](https://user-images.githubusercontent.com/124641609/224572500-bd8df539-3c22-4171-ae4b-e770951b7c45.JPG)

---

8) Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra .



---

9) Escriba un programa que reciba el nombre en minúsculas de un país de America y devuelva la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado 

1. Definimos una variable x general y con ayuda del condicional if escribiremos el pais acompañado de print donde se mostrara la capital

![capitales](https://user-images.githubusercontent.com/124641609/224579756-7534a89f-c88e-4a91-85b7-ccb9be2dff41.JPG)

--- 

10) Escriba un programa que dada una distancia calcule:






