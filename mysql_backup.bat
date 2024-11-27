
REM Cambia el directorio actual al directorio bin de MySQL Server
cd C:\Program Files\MySQL\MySQL Server 8.0\bin

REM Configura la variable "datetime" con la fecha y hora actuales en el formato YYYYMMDD_HHMMSS
REM %date% y %time% son variables de entorno que contienen la fecha y hora actuales
REM %date:~-4% obtiene los últimos 4 caracteres de la fecha (el año)
REM %date:~3,2% obtiene 2 caracteres a partir de la posición 3 de la fecha (el mes)
REM %date:~0,2% obtiene los primeros 2 caracteres de la fecha (el día)
REM %time:~0,2% obtiene los primeros 2 caracteres de la hora (las horas)
REM %time:~3,2% obtiene 2 caracteres a partir de la posición 3 de la hora (los minutos)
REM %time:~6,2% obtiene 2 caracteres a partir de la posición 6 de la hora (los segundos)
REM %datetime: =0% reemplaza los espacios en blanco en la variable datetime con ceros
set "datetime=%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "datetime=%datetime: =0%"

REM Ejecuta el comando mysqldump para hacer una copia de seguridad de la base de datos "db"
REM --user especifica el nombre de usuario de MySQL
REM --password especifica la contraseña de MySQL
REM El resultado se guarda en un archivo .sql en el directorio de respaldo con el nombre backup_YYYYMMDD_HHMMSS.sql
mysqldump --user=root --password=s3cr3t7 db > C:\Users\gabij\Documents\ssh_backup\data\backup_%datetime%.sql