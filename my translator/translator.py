from googletrans import Translator


translator = Translator()


def translate_text(text, dest='en'):
    if text and dest != "":
        return translator.translate(text, dest=dest).text
    raise ValueError("text empty")


def translate_multi_texts(dest='en', *args):
    args = translator.translate(args, dest=dest)
    return args.text


def detect_language(text):
    if (translator.detect(text).confidence) < 0.7:
        raise Exception("confidence is low")
    return translator.detect(text).lang
