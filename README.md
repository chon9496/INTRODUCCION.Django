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

#### blog/forms.py:
    from django import forms
    from .models import Post

    class PostCreateForm(forms.ModelForm):
        class Meta:
            model  = Post
            fields = ("title","content")
#### blog/views.py:
    class BlogCreateView(View):
        def get(self,request,*args, **kwargs):
            context={
            }
            return render(request,'blog_create.html',context)
        
        def post(self,request,*args, **kwargs):
            context={
            }
            return render(request,'blog_create.html',context)
#### blog/urls.py:
    path("create/", BlogCreateView.as_view(), name="create"),

### Templates:
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

## Enlistar:
·Para ello llamamos a los post de las bases de datos para 
ello dentro de la funcion get perteneciente a BlogListView
·tenemos que crear tambien nuestro blog_detail.html en 
templates
### templates/blog_list.html:
·tenemos que declarar un ciclo for y dentro de el colocamos
el post.title
·en el url que nos lleva a detail añadimos post.id porque 
en blog/urls.py usaremos "<int:pk>/" que hace referencia al id

    {% for post in posts %}
    <a href="{% url 'blog:detail' post.id %}">{{post.title}}</a>
    <br>
    {% endfor %}
    <br>
### blog/views.py:
·Creamos una nueva clase que sera para el detail

    class BlogDetailView(View):
        def get (self, request, *args, **kwargs):
            context={
                
            }
            return render(request,'blog_detail.html',context)
### blog/urls.py:
·<int:pk/> hace referencia al id que es unico el pk es el 
privatekey ese es el id y el int es numero entero

    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
#### blog/views.py
·Despues de esto en la funcion de la clase detail tenemos
que agregar pk 
·No olvidar el contexto

    def get (self, request,pk,*args, **kwargs):
        post = get_object_or_404(Post,pk=pk)
        context={
             'post':post    
        }
### templates/blog_detail.html:
·Para poder ver el contenido que hemos seleccionado solo
ponemos post. y luego lo que queremos mostrar

    {{post.title}}
    <br>
    {{post.content}}
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

## Editar:
·para editar usaremos una vista especial UpdateView
### templates:
·Crear un archivo blog_update.html
·Este template es igual al de crear asi que copiamos y pegamos


    <form method="POST">
    {% csrf_token %}
    title{{form.title}}
    <br>
    content{{form.content}}
    <button type="Submit">Update</button>  
    </form>

### blog/views.py:

Creamos la clase con UpdateView y luego escogemos el modelo x
y los campos que deseamos editar 

    model  = Post
    fields = ['title', 'content']
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗

