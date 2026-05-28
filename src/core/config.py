from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Code Helper"

    environment: str = "development"

    debug: bool = True

    api_v1_str: str = "/api/v1"

    log_level: str = "INFO"

    default_llm_provider: str = "openai"

    default_llm_model: str = "gpt-4.1-mini"

    openai_api_key: str = ""

    anthropic_api_key: str = ""

    ollama_base_url: str = "http://localhost:11434"

    enable_openai: bool = True

    enable_anthropic: bool = False

    enable_ollama: bool = False

    @property
    def is_development(self) -> bool:
        return self.environment.lower() == "development"

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
