from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Code Helper"
    environment: str = "development"
    debug: bool = True

    api_v1_str: str = "/api/v1"

    openai_api_key: str = ""
    anthropic_api_key: str = ""

    default_llm_provider: str = "openai"
    default_llm_model: str = "gpt-5"

    ollama_base_url: str = "http://localhost:11434"

    vector_db_path: str = "./data/vector_store"

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
