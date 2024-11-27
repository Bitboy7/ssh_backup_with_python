REM Configura las variables para el nombre de usuario, contraseña y nombre de la base de datos
set "MYSQL_USER=root"
set "MYSQL_PASSWORD=s3cr3t7"
set "MYSQL_DATABASE=db"
REM Configura la variable para el directorio del proyecto
set "PROJECT_DIR=C:\Users\gabij\Documents\ssh_backup"
REM Configura la variable para el directorio bin de MySQL Server
set "MYSQL_BIN_DIR=C:\Program Files\MySQL\MySQL Server 8.0\bin"

REM Cambia el directorio actual al directorio bin de MySQL Server
cd %MYSQL_BIN_DIR%

REM Configura la variable "datetime" con la fecha y hora actuales en el formato YYYYMMDD_HHMMSS
set "datetime=%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "datetime=%datetime: =0%"

REM Ejecuta el comando mysqldump para hacer una copia de seguridad de la base de datos
echo Realizando copia de seguridad de la base de datos...
mysqldump --user=%MYSQL_USER% --password=%MYSQL_PASSWORD% %MYSQL_DATABASE% > C:\Users\gabij\Documents\ssh_backup\data\backup_%datetime%.sql

REM Cambia al directorio del proyecto
echo Cambiando al directorio del proyecto...
cd %PROJECT_DIR%

REM Activa el entorno virtual de Poetry y ejecuta el script de Python
echo Ejecutando script de Python con Poetry...
poetry run python main.py

echo Script finalizado con exito.