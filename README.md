# Simulador de pagos con tarjeta de crédito.

API Rest usando Django (Python) con Docker

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
Cree el contenedor de docker
```bash
docker-compose build
docker-compose up -d
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
    "extra_description": "Test postman"
}
```
* En la pestaña de "Authorization" de Postman, selecione Bearer Token donde el Token lo optendra de la siguiente manera
- Ingrese al contenerdor a la terminal del contenedor desde Docker Desktop

Si no estás utilizando Docker Desktop, puedes usar el siguiente comando para ejecutar un shell dentro de un contenedor:
```bash
docker ps
docker exec -it <nombre_del_contenedor_o_id> /bin/sh
```

- Opten el token
```bash
python manage.py authenticate_user <username> <password>
```
Reemplaza <username> y <password> con las credenciales que deseas probar (ejemplo las credenciales del super usuario) (Usuario admin en docker-compose.yml)
<p>
<em>Nota: Recuerde que el servidor debe estar inicializado, así que abra una nueva terminal y ejecute el comando</a></em>
</p>🤓

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