import json
from .config import load_logger

logger = load_logger()


class StyleAnalyzer:
    def __init__(self, samples_path: str):
        with open(samples_path, "r") as f:
            self.samples = json.load(f).get("writing_samples", [])
        logger.info(f"Loaded {len(self.samples)} writing samples")

    def get_style_guide(self) -> str:
        word_choice = self.analyze_word_choice()
        sentence_structure = self.analyze_sentence_structure()
        tone = self.analyze_tone()

        # Format writing samples with a preceding number
        examples = "\n".join(
            [
                f"{idx + 1}. {sample['textContent']}"
                for idx, sample in enumerate(self.samples[0:10])
            ]
        )

        style_guide = (
            f"Use the following style guide: {word_choice} {sentence_structure} {tone}\n"
            "Copy the tone of the following examples:\n"
            f"{examples}"
        )
        logger.debug(f"Generated style guide: {style_guide}")
        return style_guide

    def analyze_word_choice(self) -> str:
        # Implement more sophisticated analysis here
        return "Use vivid and descriptive language. Prefer concrete nouns over abstract concepts."

    def analyze_sentence_structure(self) -> str:
        # Implement more sophisticated analysis here
        return "Vary sentence length. Use both short, punchy sentences and longer, flowing ones."

    def analyze_tone(self) -> str:
        # Implement more sophisticated analysis here
        return (
            "Maintain a reflective and introspective tone. Be personal and authentic."
        )
