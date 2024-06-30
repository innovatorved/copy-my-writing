import logging
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self, api_key: str):
        self.llm = OpenAI(api_key=api_key)

    def generate_content(self, topic: str, style_guide: str) -> str:
        prompt = PromptTemplate(
            input_variables=["topic", "style_guide"],
            template="Generate content about {topic} using the following style guide: {style_guide}"
        )
        logger.debug(f"Generating content with prompt: {prompt.template}")
        return self.llm(prompt.format(topic=topic, style_guide=style_guide))