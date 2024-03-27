import subprocess

def run_java_apps_in_docker():
    try:
        # Levantar los servicios con Docker Compose
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Servicios iniciados.")

        # Nombre del servicio Java en docker-compose.yml
        service_name = "java_app"

        # Ejecutar el primer JAR
        subprocess.run(
            ["docker-compose", "exec", "-T", service_name, "java", "-jar", "/app/jars/app1.jar"],
            check=True
        )
        print("app1.jar ejecutado.")

        # Ejecutar el segundo JAR
        subprocess.run(
            ["docker-compose", "exec", "-T", service_name, "java", "-jar", "/app/jars/app2.jar"],
            check=True
        )
        print("app2.jar ejecutado.")

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
    finally:
        # Limpiar: bajar los servicios y eliminar volúmenes
        subprocess.run(["docker-compose", "down", "-v"], check=True)
        print("Servicios y volúmenes eliminados.")

if __name__ == "__main__":
    run_java_apps_in_docker()

