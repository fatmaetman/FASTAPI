from pydantic import BaseModel

class Book(BaseModel):
    title : str
    auther : str
    image : str
    discription : str
    publish_date : str

    class Config():
        orm_mode = True

class User(BaseModel):
    name : str
    email : str
    mobile : str

    class Config():
        orm_mode = True