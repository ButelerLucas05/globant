from database.db import get_connection
from .entities.departments import Department
import pandas as pd
import math

class DepartmentModel():

    #Permite usar el metodo sin necesidad de crear una instancia de la clase
    @classmethod
    def get_departments(self):
        try:
            connection=get_connection()
            departments=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id,department from public.departments")
                dataframe = cursor.fetchall()
                for row in dataframe:
                    department = Department(row[0],row[1])
                    departments.append(department.to_json())
            connection.close()

            return departments
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_department(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT id,department from public.departments WHERE id = {id}")
                result= cursor.fetchone()
                department = None
                if result != None:
                    department = Department(result[0],result[1])
                    

            connection.close()

            return department.to_json()

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_department_from_csv(self,filename):

        try:

            ## Leemos el csv y aplicamos modificaciones
            df = pd.read_csv(filename,header=None)

            df[1]=df[1].str.replace("'"," ")
            # Cantidad de registros del DF
            registros = df.shape[0]
            # Tamaño del paginado o batch
            batch_size = 1000
            # Pagina actual que se esta recorriendo
            pagina = 1
            pagina_final = math.ceil(registros/batch_size)
            registros_finales = registros - ((pagina_final-1)*batch_size)
            query_inicial = "Insert into public.departments (id,department) VALUES"
            query = ' '
            contador = 0
            affected_rows = 0
            connection=get_connection()

            with connection.cursor() as cursor:
                

            # Por cada registro del df vamos armando el insert
                for row in df.iterrows():
                    contador = contador + 1
                    query = query + f"""(CAST({row[1][0]} AS INTEGER),'{row[1][1]}'),"""

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
