from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    
class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8080
    reload: bool = True

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api_prefix: ApiPrefix = ApiPrefix()
    
settings = Settings()
    