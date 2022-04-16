# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑

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