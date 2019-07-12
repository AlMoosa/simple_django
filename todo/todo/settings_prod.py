from .settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'simpledjango',
       'USER': 'simpledjangouser',
       'PASSWORD': '123simpledjango123',
       'HOST': 'localhost',
       'PORT': '',
   }
}