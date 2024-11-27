# Backups automáticos por ssh

![Backup](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzg4endnd241NmdhZWQwd2tzZ3pqOG80bTBpMzgyaWg3cWJ5YmpvMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/i229PTC8BKt9V9RnwZ/giphy.webp)

Este proyecto realiza copias de seguridad de una base de datos MySQL y ejecuta un script de Python utilizando Poetry.

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio desde GitHub:
    ```sh
    git clone https://github.com/Bitboy7/ssh_backup_with_python.git
    cd ssh_backup_with_python
    ```

2. Crea el archivo `.env` y configura las variables de entorno.

## Instalación de Dependencias

3. instalar las dependencias del proyecto.

(Si no tienes poetry instalado de manera global usa)
```sh
pip install poetry
```
Ejecuta el siguiente comando:
```sh
poetry install
```

4. Ejecuta el script:
    ```sh
    mysql_backup.bat
    ```

Puedes programar una tarea en Windows para ejecutar de manera automática.

## Notas

- Asegúrate de tener MySQL Server instalado y configurado correctamente.
- Modifica las variables en `mysql_backup.bat` según tus necesidades (usuario, contraseña, nombre de la base de datos y directorio del proyecto).