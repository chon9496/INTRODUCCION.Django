# INTRODUCCION.Django

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
