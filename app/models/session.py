from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.models import Base

engine = create_engine('postgresql://dbuser:users@localhost/mobileusers')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()