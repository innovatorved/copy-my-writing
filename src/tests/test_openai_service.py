import pytest
from copy_my_writing.openai_service import OpenAIService

@pytest.fixture
def openai_service():
    return OpenAIService("your_api_key_here")

def test_generate_content(openai_service):
    topic = "Your topic here"
    style_guide = "Use the following style guide: vivid and descriptive language. Prefer concrete nouns over abstract concepts. Vary sentence length. Use both short, punchy sentences and longer, flowing ones. Maintain a reflective and introspective tone. Be personal and authentic."
    content = openai_service.generate_content(topic, style_guide)
    assert isinstance(content, str)
    assert len(content) > 0