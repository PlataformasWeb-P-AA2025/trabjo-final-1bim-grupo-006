# Esta consulta obtiene la cantidad de publicaciones realizadas por cada usuario.
# Se hace un join entre Usuario y Publicacion para relacionar a cada usuario con sus publicaciones.
# Finalmente, se imprime el nombre del usuario junto con el número total de publicaciones que ha realizado.

from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

Session = sessionmaker(bind=engine)
session = Session()

publicaciones_por_usuario = session.query(
    Usuario.nombre,
    func.count(Publicacion.id).label('num_publicaciones')
).join(Publicacion).group_by(Usuario.id).order_by(desc('num_publicaciones')).all()

print("Número de publicaciones por usuario:")
for nombre, num in publicaciones_por_usuario:
    print(f"- {nombre}: {num}")