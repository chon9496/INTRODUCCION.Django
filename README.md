# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[1.0.Formularios]〕≜╠《_⋐⫸⊱┊¤⥑
·Formularios bueno este capitulo va de formularios para 
crear posts desde las vistas
·Creamos un archivo llamdo forms.py en blog y luego 
importamos el formulario creado en blog/views.py 
·En views.py creamos una nueva vista igual que la anterior
pero esta tendra 2 funciones una para get y otra para post
·En blog/urls.py  añadimos el path que le corresponde
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Forms:

### blog/forms.py:
    from django import forms
    from .models import Post

    class PostCreateForm(forms.ModelForm):
        class Meta:
            model  = Post
            fields = ("title","content")
### blog/views.py:
    class BlogCreateView(View):
        def get(self,request,*args, **kwargs):
            context={
            }
            return render(request,'blog_create.html',context)
        
        def post(self,request,*args, **kwargs):
            context={
            }
            return render(request,'blog_create.html',context)
### blog/urls.py:
    path("create/", BlogCreateView.as_view(), name="create"),

## Templates:
tenemos que crear el blog_create.html dentro de templates        
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗
