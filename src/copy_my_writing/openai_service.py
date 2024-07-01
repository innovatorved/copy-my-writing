from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from .config import load_logger

logger = load_logger()


class OpenAIService:
    def __init__(self, api_key: str, base_url: str, model: str):
        self.llm = OpenAI(
            api_key=api_key, streaming=True, base_url=base_url, model=model
        )

    def generate_content(
        self, topic: str, style_guide: str, lang: str = "hindi"
    ) -> str:
        prompt = PromptTemplate(
            input_variables=["topic", "style_guide", "lang"],
            name="copy-my-writing",
            lang=lang,
            template="You are writing tool. copy the user writing worlds style_guide to generate content. Your Primary language to generate content is {lang}. Generate poetry about {topic} in {lang} language. Using the following style guide: {style_guide}. \nEnsure the content is concise and relevant, excluding any unnecessary information",
        )
        logger.debug(f"Generating content with prompt: {prompt.template}")
        return self.llm.stream(
            prompt.format(topic=topic, style_guide=style_guide, lang=lang)
        )
