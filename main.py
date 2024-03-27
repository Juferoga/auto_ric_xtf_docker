import subprocess
from command_builder import CommandBuilder

def kill_docker():
  # Limpiar: bajar los servicios y eliminar volúmenes
  subprocess.run(["docker-compose", "down", "-v"], check=True)
  print("Servicios y volúmenes eliminados.")

def run_java_apps_in_docker():
  try:
    # Levantar los servicios con Docker Compose
    # ! por ahora no es necesario ya que se corre primero el compose
    
    # docker_compose_up = ["docker-compose", "up", "-d", "postgis"]
    # subprocess.run(docker_compose_up, check=True)
    # print("Servicios iniciados.")

    # Nombre del servicio Java en docker-compose.yml
    service_name = "java_app"

    # Ejecutar el primer comando JAR
    builder = CommandBuilder()
    command = builder.setAction("--schema-import")\
                .setDbCredentials("postgis", "5432", "postgres", "admin", "db", "postgres")\
                .setModel("/app/RIC/", "Modelo_Aplicacion_LADMCOL_RIC_V0_1")\
                .addFlags(["--setupPgExt","--createEnumTabs"])\
                .build()
    

    # Ejecutar el comando en el contenedor java_app
    docker_exec_command = ["docker-compose", "exec", service_name]+command
    a = subprocess.run(docker_exec_command, check=True)
    print(a)

    #kill_docker()

  except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e}")


if __name__ == "__main__":
    run_java_apps_in_docker()

