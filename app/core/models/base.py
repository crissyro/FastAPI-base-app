from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import Mapped, mapped_column 

class Base(DeclarativeBase):
    __abstract__ = True
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() 
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
class User(Base):
    ...
    
