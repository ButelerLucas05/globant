from database.db import get_connection
from .entities.employees import Employee
import pandas as pd
import math

class EmployeeModel():

    #Permite usar el metodo sin necesidad de crear una instancia de la clase
    @classmethod
    def get_employees(self):
        try:
            connection=get_connection()
            employees=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id,name,datetime,department_id,job_id from public.employees")
                dataframe = cursor.fetchall()
                for row in dataframe:
                    employee = Employee(row[0],row[1],row[2],row[3],row[4])
                    employees.append(employee.to_json())
            connection.close()

            return employees

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_employee(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id,name,datetime,department_id,job_id from public.employees WHERE id = {id}")
                result= cursor.fetchone()
                employee = None
                if result != None:
                    employee = Employee(result[0],result[1],result[2],result[3],result[4])
                    

            connection.close()

            return employee.to_json()

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_employee_from_csv(self,filename):

        try:

            ## Leemos el csv y aplicamos modificaciones
            df = pd.read_csv(filename,header=None)

            # Elegi llenar con datos al azar, se podrian haber omitido tambien los registros que no cumplan con las condiciones.
            df[2] = df[2].fillna('1900-01-01')
            df[4] = df[4].fillna(0)
            df[3] = df[3].fillna(0)
            df[1]=df[1].str.replace("'"," ")
            # Cantidad de registros del DF
            registros = df.shape[0]
            # Tamaño del paginado o batch
            batch_size = 1000
            # Pagina actual que se esta recorriendo
            pagina = 1
            pagina_final = math.ceil(registros/batch_size)
            registros_finales = registros - ((pagina_final-1)*batch_size)
            query_inicial = "Insert into public.employees (id,name,datetime,department_id,job_id) VALUES"
            query = ' '
            contador = 0
            affected_rows = 0
            connection=get_connection()

            with connection.cursor() as cursor:
                

            # Por cada registro del df vamos armando el insert
                for row in df.iterrows():
                    contador = contador + 1
                    query = query + f"""(CAST({row[1][0]} AS INTEGER),'{row[1][1]}','{row[1][2]}',CAST({row[1][3]} AS INTEGER),CAST({row[1][4]} AS INTEGER)),"""

                    if contador == batch_size:    
                        contador = 0
                        query = query_inicial + query[:-1]
                        print(query)
                        print("HIZO UN COMMIT DE LA QUERY DE ARRIBA Y RESETEO LA QUERY")
                        pagina = pagina + 1
                        print(f'PAGINA = {pagina}')
                        cursor.execute(query)
                        affected_rows = affected_rows + cursor.rowcount
                        connection.commit()
                        query = ' '
                    if pagina == pagina_final and contador == registros_finales:
                        query = query_inicial + query[:-1]
                        cursor.execute(query)
                        affected_rows = affected_rows + cursor.rowcount 
                        connection.commit()
                   
            connection.close()

            return affected_rows

        except Exception as ex:
            raise Exception(ex)
