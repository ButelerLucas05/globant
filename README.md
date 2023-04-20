# Ejercicio tecnico Globant

## Descripcion : 
en este proyecto se encontrara una API realizada con Python y Flask la cual permite insertar registros a 3 tablas diferentes en una instancia de base de datos PostgreSQL desde un archivo CSV y tambien permite listar los registros que se encuentran en dichas tablas.

## Requerimientos :

Dentro de la carpeta globant, se encuentra un archivo llamado requirements.txt en el cual se encuentran todas las librerias necesarias para el funcionamiento de la aplicacion,
ademas se debera contar con una instancia de base de datos PostgreSQL la cual tiene una base de datos llamada Globan y dentro del schema Public se deberan recrear las tablas cuyos DDL se encuentran en la carpeta globant/sql/ddl.
Ademas se deberan setear las crendenciales para el acceso a esta base de datos dentro del archivo  globant/.env en las variables 
-PGSQL_USER={usuario}
-PGSQL_PASSWORD={password}

## Funcionamiento :

para iniciar la aplicacion se debera  crear un entorno virtual en el cual se deberan instalar las librerias detalladas en el archivo requirements.txt,
una vez creado el entorno virtual e instaladas las librerias se debera abrir una terminal dentro de la carpeta globant y ejecutar el comando python app.py para darle inicio al servidor y poder realizar las diferentes peticiones a las URL debajo mecionadas.

1- Listar todos los registros de la tabla [GET]

- localhost:5000/api/employees
- localhost:5000/api/jobs
- localhost:5000/api/departments

2- Listar un solo registro de la tabla utilizando el id como clave , para listar se debera reemplazar la cadena {id} por el id que se desea buscar [GET]

- localhost:5000/api/employees/{id}
- localhost:5000/api/jobs/{id}}
- localhost:5000/api/departments/{id}

3- Agregar registros en base a un archivo .CSV, para esto se debera enviar dentro de un form-data el archivo csv, con el nombre file como clave, tal cual se muestra en la imagen de ejemplo que esta adjunta [POST]

![imagen](https://user-images.githubusercontent.com/47366982/233232752-9795c93f-a6fb-494a-984d-8b21eaa65385.png)

- localhost:5000/api/employees/add/csv
- localhost:5000/api/jobs/add/csv
- localhost:5000/api/departments/add/csv


# Ejercicio 2 SQL (Para este caso no tuve tiempo de disponibilizarlo mediante API, estan solo las consultas SQL):
- las consultas SQL se encuentran dentro de un archivo llamado ejercicio2.sql en la ubicacion globant/sql/


