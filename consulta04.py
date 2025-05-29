# Obtener un reporte de reacciones en función del número de veces que fueron usadas.
from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine

# crear una sesion a la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# obtenemos todas las publicaciones
publicaciones = session.query(Publicacion).all()

suma_reacciones = {}

# recorrer cada publicacion para encontrar el numero de reacciones totales de una publicacion
for pub in publicaciones:
	for reaccion in pub.reacciones:
		tipo = reaccion.tipo_emocion
		suma_reacciones [tipo] = suma_reacciones .get(tipo, 0) + 1

# Mostrar resultados
print("Reacciones y número que han sido utilizadas:")

for tipo, total in suma_reacciones .items():
	print(f"Reaccion: {tipo} - Usos: {total}")