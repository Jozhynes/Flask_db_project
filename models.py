from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer
Base=declarative_base()
class Products(Base):
    __tablename__='product'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50), nullable=False)
    description=Column(String(50), nullable=False)
    def __init__(Self, name,description):
        Self.name=name
        Self.description=description
