import re
from typing import Any


class Text:
    __text: str

    def __init__(self):
        pass

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    def clean(self) -> Any:
        text_cleaned = self.text.strip()
        text_cleaned_of_2014 = re.sub('\u2014', '-', text_cleaned)
        text_cleaned_of_u2019_u2018 = re.sub("[\u2019|\u2018]", "'", text_cleaned_of_2014)
        text_cleaned_of_u2026 = re.sub("\u2026", "...", text_cleaned_of_u2019_u2018)

        self.text = text_cleaned_of_u2026
        return self

    def clean_tags(self) -> Any:
        regex_pattern = r'(<([^>]+)>)'
        cleaner = re.sub(regex_pattern, '', self.text)

        self.text = cleaner
        return self
