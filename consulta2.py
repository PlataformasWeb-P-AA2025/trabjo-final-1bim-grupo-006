# Listar las reacciones a una publicación.

from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine


Session = sessionmaker(bind=engine)
session = Session()


publicaciones = session.query(Publicacion).all()


for publicacion in publicaciones:
    print(f"Publicación: {publicacion.contenido}")

    for reaccion in publicacion.reacciones:
        print(f"  - Reacción: {reaccion.tipo_emocion}")