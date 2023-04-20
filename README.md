## Ejercicio tecnico Globant

#Descripcion : 
en este proyecto se encontrara una API realizada con Python y Flask la cual permite insertar registros a 3 tablas diferentes en una instancia de base de datos PostgreSQL desde un archivo CSV y tambien permite listar los registros que se encuentran en dichas tablas.

#Requerimientos :
Dentro de la carpeta globant, se encuentra un archivo llamado requirements.txt en el cual se encuentran todas las librerias necesarias para el funcionamiento de la aplicacion,
ademas se debera contar con una instancia de base de datos PostgreSQL la cual tiene una base de datos llamada Globan y dentro del schema Public se deberan recrear las tablas cuyos DDL se encuentran en la carpeta globant/sql/ddl 

#Funcionamiento :

para iniciar la aplicacion se debera  crear un entorno virtual en el cual se deberan instalar las librerias detalladas en el archivo requirements.txt,
una vez creado el entorno virtual e instaladas las librerias se debera abrir una terminal dentro de la carpeta globant y ejecutar el comando python app.py para darle inicio al servidor y poder realizar las diferentes peticiones a las URL debajo mecionadas.

1- Listar todos los registros de la tabla [GET]

- localhost:5000/api/employees
- localhost:5000/api/jobs
- localhost:5000/api/departments

- Listar un solo registro de la tabla utilizando el id como clave , para listar se debera reemplazar la cadena {id} por el id que se desea buscar [GET]

1 - localhost:5000/api/employees/{id}
2 - localhost:5000/api/jobs/{id}}
3 - localhost:5000/api/departments/{id}

- Agregar registros en base a un archivo .CSV, para esto se debera enviar dentro de un form-data el archivo csv, con el nombre file como clave, tal cual se muestra en la imagen de ejemplo que esta adjunta [POST]

![imagen](https://user-images.githubusercontent.com/47366982/233232752-9795c93f-a6fb-494a-984d-8b21eaa65385.png)

1 - localhost:5000/api/employees/add/csv
2 - localhost:5000/api/jobs/add/csv
3 - localhost:5000/api/departments/add/csv


##Ejercicio 2 SQL:
- las consultas SQL se encuentran dentro de un archivo llamada ejercicio2.sql en la ubicacion globant/sql/

