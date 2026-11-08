import os
from os import reload_environ
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field, AnyHttpUrl, field_validator, ValidationError

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def _truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}

def reload() -> Settings:
    global settings
    settings = _read_settings()
    return settings

class Settings(BaseModel):
    llm_base_url: AnyHttpUrl
    llm_api_key: str = Field(min_length=1)
    llm_model: str = Field(min_length=1)
    max_input_length: int =Field(default=4000, gt=0)
    llm_stub: bool = True

    @field_validator("llm_stub", mode="before")
    @classmethod
    def _parse_bool(cls, v:object) -> object:
        return _truthy(v) if isinstance(v, str) else v

def _read_settings() -> Settings:

    try:
        return Settings(
        llm_base_url=AnyHttpUrl(os.environ["LLM_BASE_URL"]),
        llm_api_key=os.environ["LLM_API_KEY"],
        llm_model=os.environ["LLM_MODEL"],
        llm_stub=os.environ.get("LLM_STUB", "1")
    )
    except (KeyError, ValidationError) as exc:
        raise RuntimeError(
            "Missing or invalid LLM config .env — see .env.example"
        ) from exc

def get_settings() -> Settings:
    return _read_settings()


