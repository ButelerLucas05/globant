from flask import Flask
from config import config


# RUTAS
from routes import employees,jobs,departments


app = Flask(__name__)


def page_not_found(error):
    return "<h1> Ruta no encontrada </h1>", 404


if __name__ == '__main__':
    # Obtenemos el config del proyecto
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(employees.main,url_prefix = '/api/employees')
    app.register_blueprint(jobs.main,url_prefix = '/api/jobs')
    app.register_blueprint(departments.main,url_prefix = '/api/departments')

    # Cuando haya un 404 utiliza la funcion
    app.register_error_handler(404, page_not_found)
    app.run()
