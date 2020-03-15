'''

分为三个，前台，后台，公共
'''
import os
SECRET_KEY = os.urandom(24)
DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = 'hello123'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'helloflask'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %(DB_USERNAME,
            DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False



CMS_USER_ID='asdfg'

