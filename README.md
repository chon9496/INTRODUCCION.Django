# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑

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

