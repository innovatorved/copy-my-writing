import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .logger import AppLogger


@dataclass
class Config:
    openai_api_key: str
    writing_samples_path: str
    output_language: str = "hindi"


def load_config() -> Config:
    load_dotenv()
    return Config(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        writing_samples_path=os.getenv(
            "WRITING_SAMPLES_PATH", "data/writing_samples.json"
        ),
    )


def load_logger():
    app_logger = AppLogger()
    logger = app_logger.get_logger()
    return logger
