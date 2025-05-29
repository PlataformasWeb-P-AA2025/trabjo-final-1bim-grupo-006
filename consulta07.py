# Esta consulta obtiene todas las reacciones donde el usuario reaccionó a su propia publicación 
# Finalmente, se imprime el nombre del usuario y contenido de la publicación,
# y el tipo de emoción de la reacción.

from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# Crear sesión con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Obtener reacciones donde el usuario es el autor de la publicación
auto_reacciones = session.query(Reaccion).join(Usuario).join(Publicacion).filter(Reaccion.usuario_id == Publicacion.usuario_id).all()


print("Usuarios que reaccionaron a sus propias publicaciones:")
# Imprimir información de cada reacción encontrada
for reaccion in auto_reacciones:
    print(f"- Usuario: {reaccion.usuario.nombre}, Publicación: '{reaccion.publicacion.contenido[:50]}...', Emoción: {reaccion.tipo_emocion}")
