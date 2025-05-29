# Listar publicaciones de un usuario.

from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

Session = sessionmaker(bind=engine)
session = Session()

# filtro para elegir un usuario y ver sus publicaciones
usuarios = session.query(Usuario).filter(Usuario.nombre == 'Hunter').all()

print("Usuarios y sus reacciones:")

for usuario in usuarios:
    print(f"Usuario: {usuario.nombre}")
    
    for publi in usuario.publicaciones:
        print(f" Publicaciones: {publi.contenido}")
