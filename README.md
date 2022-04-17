
# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑
·Pasos para poder hacer las primeras creaciones para el 
blog tales como:
·Ambiente
·StartProject
·Usuario
·Vistas
·.env
·StartApp
·
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Ambiente:
### Instalar:
*cmd*

    pip install virtualenv env                                                                   
### Crear:
*cmd*
    
    1·-virtualenv env
    2·-python -m venv env  
### Activar:
*cmd*

    cd env/Scripts 
    activate      
    cd../..
#### Activar en Linux y mac:
*cmd*  
    
    source env/bin/activate
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## StartProject:
·En el codigo core viene a ser el nombre que le estamos 
dando al proyecto y si ponemos . al final se crea una 
carpeta y el manage.py; Si no lo colocamos se crea una 
carpeta con el nombre core y dentro de ella se crea
un archivo manage.py y una carpeta llamada core

### Requiriments:
·Crear un archivo llamado requiriments.txt y escribir:
    
    Django==4.0.4 

*cmd*

    pip install -r requiriments.txt 
### Crear:
*cmd*

    django-admin startproject core .

#### Settings:
*INSTALLED_APP* 
    
    'core',

·al hacer esta accion estamos dando persmiso a Django para
que pueda acceder a todos los otros archivos que esten 
dentro de core

·Despues de haber creado el proyecto ya podemos arrancar
con python manage.py runserver pero nos dira que tenemos
unas migraciones aparte se creara la db.sqlite3 osea la
base de datos
### Migraciones:

    python manage.py migrate

·Las migraciones son la forma en que Django propaga los 
cambios que realiza en sus modelos (agregando un campo, 
eliminando un modelo, etc.) en el esquema de su base 
de datos.
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Usuario:
para crear un usuario "simple" y lo digo asi porque puedes
crear un usuario personalizado y aprenderemos a hacer
ambos

### Usuario:
·Si nos damos cuenta este usuario puede tomar el nombre del
usuario del pc si lo dejamos en blanco al momento de 
personalizar esto dejara de ocurrir

·Una vez creado el usuario podremos ingresar como usuario
con el url /admin nos pedira usuario y contraseñaingresamos 
y todo esto es gracias a las migraciones

    python manage.py createsuperuser 
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Vistas:
·Para esto debemos de crear  

### core/views.py:
    from django.views.generic import View
    from django.shortcuts import render

    class HomeView(View):
        def get(self, request, *args, **kwargs):
            context={
                
            }
            return render(request,'',context)
### core/settings.py:
*DIRS*
    
    os.path.join('templates')

·Si... al hacer esto debemos ce crear nuestra carpeta 
templates y dentro de ella el index.html
·Ahora podemos volver a core/views.py y colocar el url 
dentro del return
### core/urls.py
·Tenemos que importar el HomeView que esta en views este 
vendria a ser la vista index es decir la del inicio
·En urlpatterns agregamos nuestro path de inxdex
en la que utilizaremos el as_view y lo utilizamos porque
estamos trabajando con una clase luego le agregamos un 
nombre
*importamos*

    from .views import HomeView

*urlpatterns* 

    path('', HomeView.as_view(), name="home"),
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## core/.env:
.Bueno esto es simple solo se tiene que crear una archivo
llamado .env dentro de la carpeta del proyecto

·Tambien debemos añenvadir esto dentro de requiriments.txt
    
    Django-environ==0.8.1

luego:
*cmd*

    pip install -r requiriments.txt

·Ahora en settings.py
*importamos*

    import environ
 
·Añadimos el sgt comando que servira para crear y leer
variables
    
    env = environ.Env()
    environ.Env.read_env()

·Cortar esto y llevarlo a .env

    SECRET_KEY=e-gmjdk4%3me7!wod5*m+f_6w%&nts@behyaka5cj#qtfg2n^i
    DEBUG=True

·Lo ramplazamos por

    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')

·Aca mismito podemos incluir otras cositas correos etc
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## StartApp:
·En el codigo blog viene a ser el nombre que le estamos 
dando a la app aca se hace toda la logica para poder
crear borrar editar y ver los articulos
·Tenemos que enlazar core y blog para eso creamos un 
archivo urls.py en blog
·En core/urls.py  creamos un path en urlspatterns
en el cual incluimos a blogs
    
### Crear:

    django-admin startapp blog
#### core/settings.py:
*INSTALLED_APP*
    
    'blog',
#### core/urls.py:
·No olvidar importar el include en django.urls

    path('blog/',include('blog.urls', namespace='blog'))
#### blog/urls.py:
    from django.urls import path

    app_name="blog"

    urlpatterns = [
        
    ]

### Vistas:
#### blog/views.py:
    from django.views.generic import View

    
    class BlogListView(View):
        def get(self,request,*args, **kwargs):
            context={

            }
            return render(request,'blog_list.html',context)
#### blog/urls.py:
    from .views import BlogListView

*urlpatterns* 

        path("", BlogListView.as_view(), name="home"),

#### Templates
en templates crearemos otro archivo blog_list.html este
sera la vista de listas
##### templates/index.html
en este html añadimos un url que nos lleve al otro html
    
    <a href={%url 'blog:home'%}>aca blog</a>
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Modelos:
·Los modelos son la infromacion que se envia a la base de
datos con los modelos podemos editar la informacion de 
manera dinamica como tambien eliminar leer o agregar
podemos crear diferentes cosas no solo post
·Al momento de crear un modelo debemos agregarlo los campos
que requiere titulo contenido y otras cosas que pueda 
o no tener
·Aca en las migraciones primero makemigrations este crea 
las migraciones 
Migrate las ejecuta las migraciones
### blog/models.py:

    class Post(models.Model):
        title=models.CharField(max_length=50)
        content=models.TextField()
### Migraciones:

    python manage.py makemigrations

    python manage.py migrate

## Admin:
·Otra cosa por hacer es que tenemos que registrar nuestros
modelos en admin para poder visualizarlo cuando entremos
como administrador
·Asi de esta manera tenemos posts en admin y gracias a ello
podemos agregar contenido o mejor dicho podemos publicar 
posts
·Toda la data se guarda en la Base de Datos

### blog/admin.py:

    from .models import Post

    admin.site.register(Post)
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗
