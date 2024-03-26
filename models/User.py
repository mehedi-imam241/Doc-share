from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    docs = relationship("Doc", back_populates="owner")
    shared_docs = relationship("SharedDoc", back_populates="user")