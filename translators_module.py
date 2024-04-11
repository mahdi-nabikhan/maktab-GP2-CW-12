import translators as ts


class Translator:

    @staticmethod
    def translate(text, source, language):
        texts = ts.translate_text(text, from_language=source, to_language=language, translator="google")
        print(texts)
