class Department():

    def __init__(self,id,department):
        self.id = id
        self.department = department


    # Creamos el json que permitira devolver los objetos en formato Json    
    def to_json(self):
        
        json_object = {
            
            'id': self.id,
            'department': self.department
        }

        return json_object