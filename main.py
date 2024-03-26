import bcrypt
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()
from database import  engine, Base


from routers.user import router as users
from routers.docs import router as items
from routers.doc_share import router as doc_share



Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users)
app.include_router(items)
app.include_router(doc_share)







