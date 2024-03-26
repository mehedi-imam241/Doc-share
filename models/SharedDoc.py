from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database import Base

class SharedDoc(Base):
    __tablename__ = "shared_docs"

    id = Column(Integer, primary_key=True)
    doc_id = Column(Integer, ForeignKey("doc.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    edit_access = Column(Boolean, default=False)

    doc = relationship("Doc", back_populates="shared_docs")
    user = relationship("User", back_populates="shared_docs")