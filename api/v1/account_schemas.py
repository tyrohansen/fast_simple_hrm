from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    id: Optional[str] = None
    username:str
    password:str
    email:str
    first_name:str
    last_name:str
    created: Optional[date] = None

    class Config:
        orm_mode=True
        allow_population_by_field_name=True
        arbitrary_types_allowed = True