from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog import schemas,models
from blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/book', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Book, db: Session =Depends(get_db)):
    new_book = models.Books(title = request.title ,auther = request.auther ,image = request.image ,discription = request.discription,publish_date = request.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book 

@app.delete('/book/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    book= db.query(models.Books).filter(models.Books.id==id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" Book with the id {id}is not available")
    
    book.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/book/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Book, db: Session = Depends(get_db)):
    BOOK =db.query(models.Books).filter(models.Books.id == id)
    if not BOOK.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" Book with the id {id}is not available")
    BOOK.update(request)
    db.commit()
    return 'updated'

@app.get('/book')
def all(db: Session = Depends(get_db)):
    book = db.query(models.Books).all()
    return book


@app.get('/book/{title}', status_code=200)
def show(title, request: schemas.Book ,db: Session =Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.title== title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with the title {title}is not available")
       # response.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog  with the id {id}is not available"}
    
    
    return book 
    

#############user
@app.post('/user', status_code=status.HTTP_201_CREATED)
def create(request:schemas.User, db: Session =Depends(get_db)):
    new_user = models.Books(title = request.title ,auther = request.auther ,image = request.image ,discription = request.discription,publish_date = request.publish_date)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    usre= db.query(models.Users).filter(models.Users.id==id)

    if not usre.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" User with the id {id}is not available")
    
    usre.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.User, db: Session = Depends(get_db)):
    User =db.query(models.Users).filter(models.Users.id == id)
    if not User.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" User with the id {id}is not available")
    User.update(request)
    db.commit()
    return 'updated'

@app.get('/user')
def all(db: Session = Depends(get_db)):
    user = db.query(models.Users).all()
    return user

@app.get('/user/{id}', status_code=200)
def show(id, request: schemas.User ,db: Session =Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id== id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id}is not available")
       # response.status_code = status.HTTP_404_NOT_FOUND
       # return {'detail': f"Blog  with the id {id}is not available"}
    
    
    return user
