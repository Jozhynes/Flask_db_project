from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
path="mysql+mysqldb://patrick:1234@localhost/Flask_app_db"
data=create_engine(path)
Session=sessionmaker(bind=data)
session=Session()