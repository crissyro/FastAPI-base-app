from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool
    is_superuser: bool


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
