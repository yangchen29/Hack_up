# encoding: utf-8

import os

use_mysql = True
base_dir = os.path.abspath(os.path.dirname(__file__))
class FlaskConfig():
    DEBUG = True
    SECRET_KEY = "S83rQ53gC4vdarcIAvY89Ky4"
    DB_URI = ''
    if use_mysql is True:
        HOST = '127.0.0.1'
        PORT = '3306'
        DATABASE = 'db1'
        USERNAME = 'user'
        PASSWORD = 'user'
        DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    else:
        DB_URI = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465 or 994
    # MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    BLOG_MAIL_SUBJECT_PREFIX = 'none'
    BLOG_MAIL_SENDER = MAIL_USERNAME
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_ENABLED = False
