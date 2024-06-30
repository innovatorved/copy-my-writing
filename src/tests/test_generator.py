import pytest
from copy_my_writing.generator import ContentGenerator

def test_generate():
    generator = ContentGenerator()
    topic = "Your topic here"
    content = generator.generate(topic)
    assert isinstance(content, str)
    assert len(content) > 0

def test_analyze_style():
    generator = ContentGenerator()
    style_guide = generator.analyze_style()
    assert isinstance(style_guide, str)
    assert len(style_guide) > 0