# Esta consulta obtiene los usuarios que han reaccionado a publicaciones que NO son suyas,
# es decir, publicaciones hechas por otros usuarios.
# Finalmente, se imprime el nombre del usuario y cuántas publicaciones ajenas ha reaccionado.

# Importar sessionmaker para crear sesiones con la base de datos
from sqlalchemy.orm import sessionmaker
# Importar func para funciones agregadas como count y distinct
from sqlalchemy import func
# Importar los modelos y el engine desde el archivo generar_tablas
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# Crear la clase Session enlazada al engine (motor de base de datos)
Session = sessionmaker(bind=engine)
# Crear una instancia de sesión para consultar la base de datos
session = Session()

# Realizar la consulta:
# - Se selecciona el nombre del usuario
# - Se cuenta cuántas publicaciones diferentes (distinct) ha reaccionado (que no sean propias)
resultados = (  # Inicia la asignación de la consulta a la variable 'resultados'
    session.query(  # Inicia una consulta con la sesión activa
        Usuario.nombre,  # Selecciona el nombre del usuario
        func.count(func.distinct(Reaccion.publicacion_id)).label("num_reacciones")  
        # Cuenta cuántas publicaciones distintas ha reaccionado el usuario
        # Se usa 'distinct' para evitar contar varias reacciones a la misma publicación
        # Se asigna un alias al conteo como 'num_reacciones'
    )
    .join(Reaccion)  # Realiza un JOIN entre Usuario y Reaccion (Usuario -> Reaccion)
    .join(Publicacion)  # Realiza un JOIN entre Reaccion y Publicacion (Reaccion -> Publicacion)
    .filter(Reaccion.usuario_id != Publicacion.usuario_id)  
    # Filtra para incluir solo las reacciones donde el usuario que reaccionó
    # no sea el mismo que publicó (reacciones a publicaciones ajenas)
    .group_by(Usuario.id)  # Agrupa los resultados por ID de usuario
    .all()  # Ejecuta la consulta y recupera todos los resultados
)


# Imprimir encabezado
print("Usuarios que han reaccionado a publicaciones de otros usuarios:")

# Recorrer los resultados e imprimir nombre y cantidad de publicaciones ajenas reaccionadas
for nombre, num in resultados:
    print(f"- {nombre}: {num} publicación(es) reaccionadas")
