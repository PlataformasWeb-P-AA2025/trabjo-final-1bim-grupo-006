# Listar las reacciones a una publicación.
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine


Session = sessionmaker(bind=engine)
session = Session()

# obtener todas las publicaciones de la base de datos
publicaciones = session.query(Publicacion).all()

# mostrar las publicaciones y sus reacciones iterando sobre cada publicacion
for publicacion in publicaciones:
    print(f"Publicación: {publicacion.contenido}")
    # obtener las reacciones de cada publicacion
    for reaccion in publicacion.reacciones:
        print(f"  - Reacción: {reaccion.tipo_emocion}")