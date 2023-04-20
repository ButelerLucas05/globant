

class Employee():

    def __init__(self,id,name,datetime,department_id,job_id):
        self.id = id
        self.name = name
        self.datetime = datetime
        self.department_id = department_id
        self.job_id = job_id

    # Creamos el json que permitira devolver los objetos en formato Json    
    def to_json(self):
        
        json_object = {
            
            'id': self.id,
            'name': self.name,
            'datetime': self.datetime,
            'departmet_id': self.department_id,
            'job_id': self.job_id
        }

        return json_object

