# Esta consulta obtiene los usuarios que han reaccionado a publicaciones que NO son suyas,
# es decir, publicaciones hechas por otros usuarios.
# Finalmente, se imprime el nombre del usuario y cuántas publicaciones ajenas ha reaccionado.

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from generar_tablas import Usuario, Publicacion, Reaccion, engine

Session = sessionmaker(bind=engine)
session = Session()

resultados = session.query(
    Usuario.nombre,
    func.count(func.distinct(Reaccion.publicacion_id)).label("num_reacciones")
).join(Reaccion).join(Publicacion).filter(
    Reaccion.usuario_id != Publicacion.usuario_id
).group_by(Usuario.id).all()

print("Usuarios que han reaccionado a publicaciones de otros usuarios:")
for nombre, num in resultados:
    print(f"- {nombre}: {num} publicación(es) reaccionadas")