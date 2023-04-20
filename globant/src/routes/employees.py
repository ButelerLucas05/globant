from flask import Blueprint, jsonify, request
from utils.utils import allowed_file, create_dir
from werkzeug.utils import secure_filename
import os

# Modelos
from models.employeeModel import EmployeeModel

main = Blueprint('employee_blueprint', __name__)


@main.route('/')
def get_employees():
    try:

        employees = EmployeeModel.get_employees()
        return jsonify(employees)
    
    except Exception as ex:

        return jsonify({'message': str(ex)}), 500
    


@main.route('/<id>')
def get_employee(id):
    try:

        employee = EmployeeModel.get_employee(id)
        if employee != None:
            return jsonify(employee)
        else: 
            return jsonify({}),404
    
    except Exception as ex:

        return jsonify({'message': str(ex)}), 500


@main.route('/add/csv',methods=['POST','GET'])
def add_employee_from_csv():
    try:

        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                print('No se encontro el archivo CSV')
                return jsonify({'message':'No se subio correctamente el archivo'}),400
            file = request.files['file']
            if file.filename == '':
                print('No se encontro el archivo CSV')
                return jsonify({'message':'No se encontro el archivo CSV'}),400
            if file and allowed_file(file.filename):

                create_dir()
                filename = secure_filename(file.filename)
                file.save(os.path.join('/files', filename))
                
                affected_rows = EmployeeModel.add_employee_from_csv(os.path.join('/files', filename))
                return jsonify({'message':f'Archivo procesado correctamente, se cargaron {affected_rows} registros'}),200
            else:
                return jsonify({'message':'Formato de archivo no admitido'}),400
            
    
    except Exception as ex:

        return jsonify({'message': str(ex)}), 500
    