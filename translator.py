from deep_translator import GoogleTranslator as Deepl


def translate(text):
    trans = Deepl(source='ru', target='en')
    return trans.translate(text)
