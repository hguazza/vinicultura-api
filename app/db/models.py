from sqlalchemy import Column, Integer, String
from .database import Base



class Commercialization(Base):
    __tablename__ = "commercializations"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    product_type = Column(String, nullable=False)
    year = Column(Integer, nullable=False, index=True)

class Processing(Base):
    __tablename__ = "processings"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    product_type = Column(String, nullable=False)
    classification = Column(String, nullable=False)
    year = Column(Integer, nullable=False, index=True)

class Production(Base):
    __tablename__ = "productions"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    product_type = Column(String, nullable=False)
    year = Column(Integer, nullable=False, index=True)