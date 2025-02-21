
# Django Blog Projecto

## Descripción
Este proyecto es una aplicación web de blog creada con Django, utilizando el patrón MVT (Modelo-Vista-Template). Incluye:
- Un modelo Post para almacenar publicaciones.
- Un formulario para agregar nuevas publicaciones.
- Un formulario de búsqueda para filtrar publicaciones por título.
- Herencia de plantillas para una mejor estructura del frontend.

## Instalación
1. Clonar el repositorio:
   sh
   git clone <URL_DEL_REPO>
   cd myblog
   
2. Crear un entorno virtual y activarlo:
   sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   
3. Instalar las dependencias:
   sh
   pip install django
   
4. Aplicar migraciones:
   sh
   python manage.py makemigrations
   python manage.py migrate
   
5. Ejecutar el servidor:
   sh
   python manage.py runserver
   

## Uso
### 1. Página de inicio
- Acceder a http://127.0.0.1:8000/.
- Se muestra una lista de publicaciones existentes.
- Se puede realizar una búsqueda por título.

### 2. Agregar una nueva publicación
- Ir a http://127.0.0.1:8000/new/.
- Completar el formulario con el título y contenido.
- Guardar la publicación y ser redirigido a la página de inicio.

### 3. Estructura de archivos importantes
- *models.py*: Define la clase Post.
- *forms.py*: Contiene los formularios PostForm y SearchForm.
- *views.py*: Maneja la lógica para listar, buscar y agregar posts.
- *templates/*: Contiene base.html, index.html y post_form.html para la estructura de las páginas.
- *urls.py*: Define las rutas principales.

## Subir cambios a GitHub
Para actualizar el repositorio:
sh
   git add .
   git commit -m "Actualización del blog"
   git push origin main