from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    name:str
    location:str

class CompanyUpdate(BaseModel):
    name:Optional[str]=None
    salary:Optional[str]=None