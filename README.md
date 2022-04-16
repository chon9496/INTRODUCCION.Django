# INTRODUCCION.Django

# ⌘⥏¤┊⊰⫷⋑_》╣≜〔[0.0.Creaciones]〕≜╠《_⋐⫸⊱┊¤⥑

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
