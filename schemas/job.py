from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title:(Optional[str]=True)
    salary:(Optional[str]=True)


class JobUpdate(BaseModel):
    name:Optional[str]=True
    salary:Optional[str]=True