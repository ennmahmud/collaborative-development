import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
<<<<<<< HEAD
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
       # 'postgresql://postgres:collabdev212@localhost:5432/wlvapp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///wlvapp.db'  # This creates a file named wlvapp.db in your project directory
=======
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://openday_fkgj_user:UQfth8yMO3ub8WHjTd0GJeU9lIGb7Swo@dpg-d0g7b4juibrs73fb2mg0-a.oregon-postgres.render.com/openday_fkgj')
>>>>>>> 72389a80a0e3415bcace6a7a989abe794bfc356e
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-dev-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
