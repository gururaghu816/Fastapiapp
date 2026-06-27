from sqlalchemy import Column,Integer,String,Enum
from database import Base,engine,SessionLocal
from models.

Base = declarative_base()
class Company(Base):
    __tablename__="companies"
    id = Column(Integer,primary_key=True,Integer=True,index=True)
    email = Column(unique=True)
    phone = Column(unique=True)
    jobs = relationship("jobs",
    back_populates="company")