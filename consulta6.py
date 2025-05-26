# Esta consulta busca todos los usuarios que NO tienen publicaciones asociadas.
# Luego imprime el nombre de cada uno de estos usuarios.

from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine


Session = sessionmaker(bind=engine)
session = Session()

usuarios_sin_publicaciones = session.query(Usuario).filter(~Usuario.publicaciones.any()).all()

print("Usuarios sin publicaciones:")

for user in usuarios_sin_publicaciones:

    print(f"- {user.nombre}")