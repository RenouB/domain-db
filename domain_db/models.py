from sqlalchemy import Float, Column, DateTime, String, Integer, func  
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gemuese(Base):  
    __tablename__ = 'gemuese'
    id = Column(Integer, primary_key=True)
    typ = Column(String(255))
    cultivator = Column(String(255))
    laenge = Column(Float)
    preis = Column(Float)
    
    def __repr__(self):
        return 'id: {}, type: {}, cultivator: {}'.format(self.id, self.typ, self.cultivator)