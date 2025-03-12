from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    ) 

class DatabaseHelper:
    def __init__(self, 
                 url: str, 
                 echo: bool = False, 
                 echo_pool: bool = False,
                 max_overflow: int = 10,
                 pool_size: int = 5
                 ) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, 
                echo=echo, 
                echo_pool=echo_pool,
                max_overflow=max_overflow,
                pool_size=pool_size
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, 
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
        
    async def disposw(self) -> None: 
        await self.engine.dispose()