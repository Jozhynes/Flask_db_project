from models import Base
from connection import data
Base.metadata.create_all(bind=data)