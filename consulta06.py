# Esta consulta busca todos los usuarios que NO tienen publicaciones asociadas.
# Luego imprime el nombre de cada uno de estos usuarios.

from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# Crear una sesion a la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Se realiza una consulta para obtener todos los usuarios cuya relación 'publicaciones' esté vacía
# El operador ~ se usa para negar la condición 'Usuario.publicaciones.any()'
usuarios_sin_publicaciones = session.query(Usuario).filter(~Usuario.publicaciones.any()).all()

# Se imprime un encabezado indicando que se listarán los usuarios sin publicaciones
print("Usuarios sin publicaciones:")

# Se itera sobre la lista de usuarios obtenidos y se imprime el nombre de cada uno
for user in usuarios_sin_publicaciones:
    print(f"- {user.nombre}")
