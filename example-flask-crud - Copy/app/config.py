import os
basedir = os.path.abspath(os.path.dirname(file))

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    # You can uncomment the next line if you're using environment variables for your SECRET_KEY
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:OFSDFSFssfkljfsf45464@db-sg.czmw22mmmd2b.us-east-1.rds.amazonaws.com:3306/notes'

    SQLALCHEMY_TRACK_MODIFICATIONS = False