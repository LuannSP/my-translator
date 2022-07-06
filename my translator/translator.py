from googletrans import Translator
from typing import Any, List

translator = Translator()

def translate_text(elem: str, dest: str = "en") -> Any:
    if type(elem) != str:
        return elem
    if elem and dest != "":
        return translator.translate(elem, dest=dest).text
    raise ValueError("text empty")


def translate_multi_texts(dest: str = "en", *args: str) -> List:
    args = translator.translate(args, dest=dest)
    return args.text


def detect_language(elem: str) -> (Any | str):
    if (translator.detect(elem).confidence) < 0.7:
        raise Exception("confidence is low")
    return translator.detect(elem).lang
