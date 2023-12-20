# Simulador de pagos con tarjeta de crédito.

API Rest usando Django (Python).

## Instalación
Cree un entorno virtual en Python, puede utilizar la herramienta venv, donde nombre_del_entorno es el nombre que le deseas dar al entorno virtual. 
```bash
python -m venv nombre_del_entorno
```
Active el entorno virtual. La forma de activar el entorno virtual depende del sistema operativo:
* En Windows:
```bash
armaTuVaca-env\Scripts\activate
```
* En Unix o MacOS:
```bash
source armaTuVaca/bin/activate
```
Clone el repositorio
```bash
git clone git@github.com:lihuesom/api_payment.git
```
Instale las dependencias
```bash
pip install -r requirements.txt
```
Ejecute las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
Cree un super usuario (Opcional): 
Siga los pasos de [docs.djangoproject](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)


Cambie las credenciales a su base de datos PostgreSQL en el archivo .env
```python
DB_DEFAULT_NAME = BD_name
DB_DEFAULT_USER = user_name
DB_DEFAULT_PASSWORD= pass
DB_DEFAULT_HOST = localhost
DB_DEFAULT_PORT = 5432
```
Inicie el Servidor de Desarrollo:
```bash
python manage.py runserver
```
## Uso
### Abrir Postman
* Abra Postman y cree una nueva solicitud POST.
* Ingresa la URL  http://127.0.0.1:8000/api/payment-tc/process.
* Selecciona el cuerpo (Body) y el formato (raw).
* Inserta el JSON de ejemplo en el cuerpo de la solicitud:

```json
{
    "name": "Patricia",
    "surname": "Pinzon",
    "card_number": "12345678585",
    "card_cvv": "125",
    "total_value": 1,
    "extra_description": "Test 3 postman"
}
```
* Haz clic en "Send" para realizar la solicitud.

## Contribuir
Este es un proyecto un prueba de como poder realizar un simulador de pagos, aún así las solicitudes Pull requests son bienvenidas. 

Recuerde seguir estos pasos:

Fork el repositorio
Crea una rama para tu nueva característica: git checkout -b nueva-caracteristica
Realiza tus cambios y haz commit: git commit -m "Añadir nueva característica"
Push a tu rama: git push origin nueva-caracteristica
Abre un Pull Request en GitHub

## License
[MIT](https://choosealicense.com/licenses/mit/)