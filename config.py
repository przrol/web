import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="postgre-chapter3.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="rpadmin@postgre-chapter3" #TODO: Update value
    POSTGRES_PW="Udacity123"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://servicebus-rp.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=MksPQBREtHaVtmapjvaiUyO8xwoUDh7gxaPHk08PVEc='
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS = 'rolandprz@gmx.de'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False