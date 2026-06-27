from sqlalchemy import Column,Integer,String,Enum,ForeignKey
from models.company import Company,relationship
from database  import Base,engine,SessionLocal


class Job(Base):
    __tablename__="jobs"
    id = Column(Integer,primary_key=True,Integer=True)
    title = Column(String,nulltable=False)
    decription = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey{"companies_id"})

    company=relationship("Company",back_populates="jobs")