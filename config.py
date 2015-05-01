import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/grampy'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
print(SQLALCHEMY_DATABASE_URI)
SECRET_KEY = '5E3Lkip847$H$PawMf489tVEa#eCU67KIJ}438mpG[nWaOV<u8g:ydC9RMs'

# pagination
POSTS_PER_PAGE = 3

#file upload 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#file path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/static/assets/uploads')

