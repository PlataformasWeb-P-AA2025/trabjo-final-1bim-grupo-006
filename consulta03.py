# Mostrar en qué publicaciones reaccionó un usuario.
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine


Session = sessionmaker(bind=engine)
session = Session()

# usamos un filtro para elegir un usuario en especifico
usuarios = session.query(Usuario).filter(Usuario.nombre == 'Deanna').all()

# presentar los usuarios y sus reacciones, iterando sobre cada usuario
print("Usuarios y sus reacciones:")
for u in usuarios:
    print("Usuario:", u.nombre)
    # iterar cada reaccion, para obtenerla y presentarla
    for reaccion in u.reacciones:
        print(" - Reaccionó a:", reaccion.publicacion.contenido)
        print(" - Emoción:", reaccion.tipo_emocion)
    print("---------")