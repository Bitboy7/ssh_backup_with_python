import os
import datetime
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from dotenv import load_dotenv

load_dotenv()

def ssh_copy_folder_with_password():
    # Cargar las variables de entorno
    server_host = os.getenv("SSH_SERVER_HOST")  # Dirección IP o nombre del servidor
    server_port = int(os.getenv("SSH_SERVER_PORT", 22))  # Puerto SSH, por defecto 22
    username = os.getenv("SSH_USERNAME")  # Usuario SSH
    password = os.getenv("SSH_PASSWORD")  # Contraseña SSH
    local_folder = os.getenv("LOCAL_FOLDER_PATH")  # Carpeta local a copiar
    remote_path = os.getenv("REMOTE_FOLDER_PATH")  # Carpeta destino en el servidor
    backup_folder = os.getenv("BACKUP_FOLDER")  # carpeta de respaldo alterna

    # Verificar que todas las variables estén configuradas
    if not all([server_host, username, password, local_folder, remote_path]):
        print("Error: Faltan variables de entorno necesarias. Por favor, configúralas.")
        return

    # Calcular la fecha límite (hace tres días)
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=3)

    try:
        # Crear conexión SSH
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=server_host, port=server_port, username=username, password=password)

        # Crear cliente SCP
        with SCPClient(ssh.get_transport()) as scp:
            print(f"Copiando archivos de respaldo de hace tres días de '{local_folder}' al servidor...")

            # Filtrar y copiar archivos modificados hace tres días
            for root, dirs, files in os.walk(local_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_mtime >= cutoff_date:
                        remote_file_path = os.path.join(remote_path, os.path.relpath(file_path, local_folder))
                        scp.put(file_path, remote_file_path, recursive=True, preserve_times=True)
                        print(f"Archivo '{file_path}' copiado exitosamente a '{remote_file_path}' en el servidor.")

                        # Copiar también a la carpeta de respaldo local
                        backup_file_path = os.path.join(backup_folder, os.path.relpath(file_path, local_folder))
                        os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
                        os.system(f'copy "{file_path}" "{backup_file_path}"')
                        print(f"Archivo '{file_path}' copiado exitosamente a '{backup_file_path}' en la carpeta de respaldo local.")

    except Exception as e:
        print(f"Error al copiar los archivos: {e}")

    finally:
        # Cerrar conexión SSH
        ssh.close()

if __name__ == "__main__":
    ssh_copy_folder_with_password()
