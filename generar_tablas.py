from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Importar cadena de conexión
from configuracion import cadena_base_datos

# Crear motor
engine = create_engine(cadena_base_datos)

# Declarar base
Base = declarative_base()

# Clase intermedia: Reacción (tipo emoción entre usuario y publicación)
class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    tipo_emocion = Column(String(50), nullable=False)

    usuario = relationship("Usuario", back_populates="reacciones")
    publicacion = relationship("Publicacion", back_populates="reacciones")

    def __repr__(self):
        return "Reaccion: usuario=%s, publicacion=%s, tipo_emocion=%s" % (
            self.usuario.nombre,
            self.publicacion.contenido[:30] + "...",
            self.tipo_emocion
        )

# Clase Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)

    publicaciones = relationship("Publicacion", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")

    def __repr__(self):
        return "Usuario: nombre=%s" % (self.nombre)

# Clase Publicación
class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    contenido = Column(Text, unique=True, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

    def __repr__(self):
        return "Publicacion: contenido=%s..." % (self.contenido[:30])

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)
