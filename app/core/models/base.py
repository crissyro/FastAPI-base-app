from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column 

class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    
class User(Base):
    ...
    
