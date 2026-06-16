from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

load_dotenv()
# Print to see what's loaded
#


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    api_key: str
    url: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",  # Optional: ignore extra fields
    )


settings = Settings()
