from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    
class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api_prefix: ApiPrefix = ApiPrefix()
    
settings = Settings()
    