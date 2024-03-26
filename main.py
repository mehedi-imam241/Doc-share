import bcrypt
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
from database import  engine, Base


from routers.user import router as users
from routers.docs import router as items
from routers.doc_share import router as doc_share



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Docs API",
    description="The API system for a document management tool will allow users to create, update, and delete documents. Users can also share documents with others and manage their access rights. The system will be developed using FastAPI and SQLAlchemy ORM, with JWT for user authentication and authorization. The API endpoints will be grouped and documented using Swagger UI.",
    summary="It enables document operations and sharing, developed using FastAPI and SQLAlchemy ORM, with JWT for user authentication",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Mehedi Imam",
        "email": "mehediimam1805039@outlook.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


app.include_router(users)
app.include_router(items)
app.include_router(doc_share)







