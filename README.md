# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑


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
