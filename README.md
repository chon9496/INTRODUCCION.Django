# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑

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
base de 
### Migraciones:

    python manage.py migrate

·Las migraciones son la forma en que Django propaga los 
cambios que realiza en sus modelos (agregando un campo, 
eliminando un modelo, etc.) en el esquema de su base 
de datos.
## ⋖⥐⋗⫷·.·⫸○⫷⫸█■¯Δ|Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ|Δ¯■█⫷⫸○⫷·.·⫸⋖⥐⋗