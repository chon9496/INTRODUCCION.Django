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

## Crear:

### templates/blog_list.html:
·Añadimos esto para poder llegar a crear
    <br>
    <a href="{% url 'blog:create' %}">create</a>
### blog/views.py:
por fin usaremos aca el blog/views.py para ello
lo greagamos primero al get

    form = PostCreateForm()

y dentro del contexto 

    'form':form
### templates/blog_create.html:
en esta parte hacemos el llamado form. y luego lo que 
queremos ver o mostrar

    create
    <form method="POST">
    {% csrf_token %}
    title{{form.title}}
    <br>
    content{{form.content}}
    <button type="Submit">Submit </button>  

    </form>
### blog/views.py:
·Ya lo implementamos en la funcion get ahora toca en la
funcion post para ello importamos from .models import Post

    from .models import Post

·Si el metodo es post pedimos el formulario y si este es valido obtenemos sus datos ahora podemos crear el post para eso utilizamos la lines de comando de p,created = ...
pasandole al final los campos de post
·Luego guardamos con p.save() y para finalizar retornamos el valor con redirect para que nos lleve a la pagina 
del blog

    if request.method=='POST':
        form= PostCreateForm(request.POST)
        if form.is_valid():
            title   = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
                
            p,created = Post.objects.get_or_create(title=title,content=content)

            p.save()

            return redirect('blog:home')   
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗
