from sqlalchemy.orm import sessionmaker
from generar_tablas import Usuario, Publicacion, Reaccion, engine


Session = sessionmaker(bind=engine)
session = Session()

usuarios_con_actividad = session.query(Usuario).filter(Usuario.nombre == 'Justin').all()
for user in usuarios_con_actividad:
        print(f"----------------------------------------------")
        print(f"Usuario: {user.nombre}")
        if user.publicaciones:
            print("  Publicaciones:")
            for pub in user.publicaciones:
                # Formato similar a "nombre_pais - Lenguaje: lenguajes"
                print(f"    - '{pub.contenido[:60]}...' - Fecha: {pub.fecha.strftime('%Y-%m-%d %H:%M')}")
                if pub.reacciones:
                    print("      Reacciones a esta publicación:")
                    for reaction in pub.reacciones:
                        print(f"        -> De {reaction.usuario.nombre}: '{reaction.tipo_emocion}'")
                else:
                    print("      (Sin reacciones para esta publicación)")
        else:
            print("  (No tiene publicaciones)")