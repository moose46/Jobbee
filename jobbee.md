# Install Software
* Python
* Postgres
* Nextjs
* Vs Code
* Postman


## Create venv
```
pip install virtualenv
virtualenv myenv
source myenv/scripts/activate
pip install django
django-admin startproject backend
python -m pip install --upgrade pip
pip install boto3 django-cors-headers django-dotenv django-filter django-storages djangorestframework djangorestframework-simplejwt geocoder gunicorn whitenoise psycopg2 dj-dqtabase-url
```
```
$ pip list
Package         Version
--------------- -------
asgiref         3.6.0
boto3           1.26.64
botocore        1.29.64
Django          4.1.6
jmespath        1.0.1
pip             23.0
psycopg2        2.9.5
python-dateutil 2.8.2
s3transfer      0.6.0
setuptools      65.6.3
six             1.16.0
sqlparse        0.4.3
tzdata          2022.7
urllib3         1.26.14
wheel           0.38.4

```
## Postgress
* create database
* pgadmin4 create databse jobbee user=postgres

## Settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "jobbee-api",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "locahost",
        'PORT': 5432
    }
} 
Add to ...
INSTALLED_APPS = [
    ........
    'django.contrib.gis',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
VIRTUAL_ENV_BASE = os.environ.get('VIRTUAL_ENV')
GEOS_LIBRARY_PATH = VIRTUAL_ENV_BASE + '/Lib/site-packages/osgeo/geos_c.dll'
GDAL_LIBRARY_PATH = VIRTUAL_ENV_BASE + '/Lib/site-packages/osgeo/gdal304.dll'

``` 
## Install GIS
* Stackbuilder Spactial GIS
* Install the GDAL file, python 3.11 and win 64 
''' https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
'''
* move the file to backend directory
```
$ pip install GDAL-3.4.3-cp311-cp311-win_amd64.whl 
Processing c:\users\me\vscodeprojects\tronics\backend\gdal-3.4.3-cp311-cp311-win_amd64.whl
Installing collected packages: GDAL
Successfully installed GDAL-3.4.3
```
# Run Server
```
cd backend
python manage.py manageserver
```
# Install Django OSGeoW
```
https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/
https://trac.osgeo.org/osgeo4w/
```

