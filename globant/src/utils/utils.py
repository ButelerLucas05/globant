import datetime
import os

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'csv'}

def create_dir() -> bool:
      try:
        os.makedirs('/files')
        return True
      except:
        return True


def convert_date(date) -> str:
        return datetime.datetime.strftime(date,'%d/%m/%Y')
    

def allowed_file(filename) -> str:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

