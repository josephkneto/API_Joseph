from sqlalchemy import Column, Integer, String
from .database import Base

class Member(Base):
    __tablename__ = "member"  # Use double underscores for __tablename__

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    quote = Column(String(50), index=True)

