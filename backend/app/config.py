from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    LEMON_SQUEEZY_API_KEY: str
    LEMON_SQUEEZY_STORE_ID: str
    LEMON_SQUEEZY_VARIANT_ID: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()