# Listar todas las reacciones de 
# tipo "alegre", "enojado", "pensativo" 
# que sean de usuarios que cuyos nombre no inicien con vocal.

from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, func
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# crear una sesion a la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Emociones que queremos filtrar
emociones = ["alegre", "enojado", "pensativo"]

# Vocales para excluir (usuarios cuyo nombre NO comienza con estas letras)
vocales = ('A', 'E', 'I', 'O', 'U')

# Crear la condición para nombres que NO empiecen con vocal
condicion_vocales = ~or_(
    *[func.upper(func.substr(Usuario.nombre, 1, 1)) == v for v in vocales]
)

# Consulta: reacciones con emociones filtradas y nombre del usuario que no inicia con vocal
reacciones = session.query(Reaccion).join(Reaccion.usuario).filter(
    Reaccion.tipo_emocion.in_(emociones),
    condicion_vocales
).all()

# Mostrar resultados
for reaccion in reacciones:
    print(f"{reaccion.usuario.nombre} - {reaccion.tipo_emocion}")