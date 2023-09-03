from blog.database import Base
from sqlalchemy import Column, String,Integer

class Books(Base):
    __tablename__ = 'Books'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    auther = Column(String)
    image = Column(String)
    discription = Column(String)
    publish_date = Column(String)

class Users(Base):
    __tablename__='Users'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    mobile = Column(String)