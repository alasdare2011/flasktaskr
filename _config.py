import os #misc. operating systems interface

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flasktaskr.db"
USERNAME = "admin"
PASSWORD = "admin"
WTF_CSRF_ENABLED = True #used for cross-site request forgery prevention
SECRET_KEY = "us6'rhmM+fTrWB8p" #used in conjunction with WTF_CSRF_ENABLED
                                #to create a cryptographic token 
                                #to validate a form 

#define the full path of the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

