from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_HOST: str
    DB_PORT: str
    DB_PASS: str

    @property
    def DATABASE_URL(self):
        return f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = '.env'  # Path to your .env file
        env_file_encoding = 'utf-8'


settings = Settings()
