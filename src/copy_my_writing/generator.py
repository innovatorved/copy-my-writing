from .openai_service import OpenAIService
from .style_analyzer import StyleAnalyzer
from .config import load_logger

logger = load_logger()

class ContentGenerator:
    def __init__(self, config):
        self.config = config
        self.openai_service = OpenAIService(config.openai_api_key)
        self.style_analyzer = StyleAnalyzer(config.writing_samples_path)

    def generate(self, topic: str) -> str:
        logger.info(f"Generating content for topic: {topic}")
        style_guide = self.style_analyzer.get_style_guide()
        content = self.openai_service.generate_content(topic, style_guide)
        logger.debug(f"Generated content: {content[:100]}...")  # Log first 100 chars
        return content