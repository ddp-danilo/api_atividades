from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///programador_habilidades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programadores(Base):
    __tablename__='programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)
    email = Column(String(320))

class Habilidades(Base):
    __tablename__='habilidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))

class Programador_Habilidade(Base):
    __tablename__='programador_habilidades'
    id = Column(Integer, primary_key=True)
    id_programador = Column(Integer, ForeignKey('programadores.id'))
    id_habilidade = Column(Integer, ForeignKey('habilidades.id'))
    programador = relationship('Programadores')
    habilidade = relationship('Habilidades')

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()