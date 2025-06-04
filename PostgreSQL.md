Conexión a PostgreSQL a través de Docker

- Primero instalar Docker, con los siguientes comandos:
sudo apt update
sudo apt install docker.io -y

- Habilitar Docker y levantarlo:
sudo systemctl enable docker
sudo systemctl start docker

- Instalar PostgreSQL, con los siguientes comandos 
sudo apt update
sudo apt install postgresql postgresql-contrib -y

- CREAR un usuario en PostgreSQL 
usuario: raul
contraseña: raul8005

------------------------------------------------------

- El contenedor (comando) que se debe ejecutar es el siguiente

sudo docker run --name postgres_container \
  -e POSTGRES_USER=raul \
  -e POSTGRES_PASSWORD=raul8005 \
  -e POSTGRES_DB=premier_league \
  -p 5433:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres

- Para probar la conexión se puede usar el siguiente comando:

psql -h localhost -p 5433 -U raul -d premier_league
requiere contraseña: raul8005

- Una vez realizado eso se puede generar las tablas y cargar datos

sudo -u postgres psql