import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .logger import AppLogger


@dataclass
class Config:
    openai_api_key: str
    writing_samples_path: str
    output_language: str
    openai_base_url: str
    model: str


def load_config() -> Config:
    load_dotenv()
    return Config(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        writing_samples_path=os.getenv(
            "WRITING_SAMPLES_PATH", "data/writing_samples.json"
        ),
        output_language=os.getenv("OUTPUT_LANGUAGE", "hindi"),
        openai_base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
        model=os.getenv("MODEL", "gpt-3.5-turbo-instruct"),
    )


def load_logger():
    app_logger = AppLogger()
    logger = app_logger.get_logger()
    return logger
