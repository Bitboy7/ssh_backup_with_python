# Proyecto de Copia de Seguridad MySQL

Este proyecto realiza copias de seguridad de una base de datos MySQL y ejecuta un script de Python utilizando Poetry.

## Instalación de Dependencias

Para instalar las dependencias del proyecto, ejecuta el siguiente comando:

```sh
poetry install
```

## Ejecución del Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio desde GitHub:
    ```sh
    git clone https://github.com/Bitboy7/ssh_backup_with_python.git
    cd ssh_backup_with_python
    ```

2. Crea el archivo `.env` y configura las variables de entorno.

3. Ejecuta el script:
    ```sh
    mysql_backup.bat
    ```

Puedes programar una tarea en Windows para ejecutar de manera automática.

## Notas

- Asegúrate de tener MySQL Server instalado y configurado correctamente.
- Modifica las variables en `mysql_backup.bat` según tus necesidades (usuario, contraseña, nombre de la base de datos y directorio del proyecto).