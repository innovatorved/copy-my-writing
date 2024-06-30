import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class Config:
    openai_api_key: str
    writing_samples_path: str

def load_config() -> Config:
    load_dotenv()
    return Config(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        writing_samples_path=os.getenv("WRITING_SAMPLES_PATH", "data/writing_samples.json")
    )