1) First check python version: python --version

2) If 2.7 install latest version(3.5): sudo apt-get install python3-pip

3) Now make python3.5 the system version: 
    i) update-alternatives --list python
    If the above gives "update-alternatives: error: no alternatives for python" then list the python versions first

        a) update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
        b) update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2

4)Again check python version now it should be 3.5

5)Now check pip version using: pip --version 
    it should show: "pip 9.0.1 from /usr/local/lib/python3.5/dist-packages (python 3.5)"

6)Now install Django using: pip install django

7)Check Django version: django-admin --version
    it should show: "1.10.4"

8)Install MysqlDb for python3: sudo apt-get install python3-mysqldb

9)Install Mysql Connector for python3: sudo pip install --upgrade mysql-connector-python3

----DONE----

Create Project:
django-admin startproject projectname

Migrate DB:
cd projectname
python manage.py makemigrations
python manage.py migrate

Check if it worked:
python manage.py runserver
Open localHost to check

Create app:
python manage.py startapp appname


Create App:
cd projectname
django-admin startproject projectname

To import:
1) In settings.py: 
    import MySQLdb

To replace:
1) In settings.py
    i) DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stores', #your db name
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': 'localhost',
    'OPTIONS': {
        'sql_mode': 'STRICT_TRANS_TABLES',
        },
    }
}

    ii) INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AccessMasterGridView', #your app name
]

    iii) TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

To create:
1) One templates folder in the project folder for things like html etc. (beside your app folder)
2) One static folder in the project folder for things like css,images etc. (beside your app folder)
3) urls.py in your app folder

To write:
1) Inside project folder in urls.py
    from django.conf.urls import url, include
    from django.contrib import admin

urlpatterns = [
    url(r'^', include('AccessMasterGridView.urls')), # Inside inculde your app_name.urls
    url(r'^admin/', admin.site.urls),
]

2) Inside app folder in urls.py
    from django.conf.urls import url
    from AccessMasterGridView import views  # Your app view

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),  # Class inside your view.py
    url(r'^about/$', views.AboutPageView.as_view()),  # Class inside your view.py
]


# For getting the table models of already made data_base use:  python manage.py inspectdb
 



