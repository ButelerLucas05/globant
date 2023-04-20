
class Job():

    def __init__(self,id,job):
        self.id = id
        self.job = job


    # Creamos el json que permitira devolver los objetos en formato Json    
    def to_json(self):
        
        json_object = {
            
            'id': self.id,
            'job': self.job
        }

        return json_object