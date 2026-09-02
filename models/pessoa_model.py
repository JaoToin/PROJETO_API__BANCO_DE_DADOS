from sqlalchemy import Column, Integer, String, DECIMAL, Date

from database import Base

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    idpessoa = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    datanascimento = Column(Date)
    peso = Column(Integer)
    altura = Column(DECIMAL(10,2))
    sexo = Column(String(1))
    
    
   

