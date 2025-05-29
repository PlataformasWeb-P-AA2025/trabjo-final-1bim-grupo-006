# Esta consulta obtiene el top 4 de usuarios que han dado más reacciones a publicaciones no necesariamente propias.
# Se cuenta cuántas veces cada usuario ha reaccionado
# Finalmente, se imprime el nombre de cada usuario junto con la cantidad de reacciones que ha hecho.

from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# Crear sesión con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Consultar nombre del usuario y contar cuántas reacciones ha dado
reacciones_por_usuario = session.query(
    Usuario.nombre,
    func.count(Reaccion.publicacion_id).label('num_reacciones')
).join(Reaccion).group_by(Usuario.id).order_by(desc('num_reacciones')).limit(4).all()

# Imprimir el top 4 de usuarios con más reacciones
print("Top 4 usuarios con más reacciones dadas:")
for nombre, num in reacciones_por_usuario:
    print(f"- {nombre}: {num}")