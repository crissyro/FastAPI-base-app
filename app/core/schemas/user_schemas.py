
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool
    last_login_at: datetime
    created_at: datetime
    
class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int