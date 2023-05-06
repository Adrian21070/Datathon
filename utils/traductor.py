from typing import Sequence, List
from deep_translator import GoogleTranslator


class DataTranslator(object):
    """
    Data Translator Class.
    Uses the Google API library.
    """

    def __init__(self) -> None:
        self._translator = GoogleTranslator(source="auto", target="en")

    def translate(self, text_batch: Sequence[str]) -> List[str]:
        if not isinstance(text_batch, (list, tuple, set)):
            raise ValueError("An iterable it's expected")

        translated_batch = self._translator.translate_batch(
            batch=text_batch
        )

        return translated_batch