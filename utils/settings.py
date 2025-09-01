from pydantic_settings import BaseSettings
from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    """Manages application settings and environment variables."""

    gemini_api_key: Optional[SecretStr] = Field(default=None, alias="GOOGLE_API_KEY")
    gcp_project: Optional[str] = Field(default=None, alias="GCP_PROJECT")
    gcp_location: Optional[str] = Field(default=None, alias="GCP_LOCATION")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

settings = Settings()
