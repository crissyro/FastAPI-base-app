
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool
    last_login_at: datetime
    created_at: datetime
    
class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    
    id: int