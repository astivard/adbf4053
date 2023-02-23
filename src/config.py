from os import getenv, path

from dotenv import load_dotenv

env_location = path.join((path.abspath(path.dirname(path.dirname(__file__)))), '.env.sample')
load_dotenv(env_location)

SECRET_KEY = getenv('SECRET_KEY')

DATABASE = getenv('DATABASE')
DB_USER = getenv('DB_USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')
PORT = getenv('PORT')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
