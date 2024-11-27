import os
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

    # Verificar que todas las variables estén configuradas
    if not all([server_host, username, password, local_folder, remote_path]):
        print("Error: Faltan variables de entorno necesarias. Por favor, configúralas.")
        return

    try:
        # Crear conexión SSH
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=server_host, port=server_port, username=username, password=password)

        # Crear cliente SCP
        with SCPClient(ssh.get_transport()) as scp:
            print(f"Copiando la carpeta '{local_folder}' al servidor...")
            scp.put(local_folder, remote_path, recursive=True, preserve_times=True)
            print(f"Carpeta '{local_folder}' copiada exitosamente a '{remote_path}' en el servidor.")

    except Exception as e:
        print(f"Error al copiar la carpeta: {e}")

    finally:
        # Cerrar conexión SSH
        ssh.close()

if __name__ == "__main__":
    ssh_copy_folder_with_password()
