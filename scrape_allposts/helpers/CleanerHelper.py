import re


class CleanerHelper:
    def __int__(self):
        pass

    def clean(self, text: str) -> str:
        text_cleaned = text.strip()
        text_cleaned_of_2014 = re.sub('\u2014', '-', text_cleaned)
        text_cleaned_of_u2019_u2018 = re.sub("[\u2019|\u2018]", "'", text_cleaned_of_2014)
        text_cleaned_of_u2026 = re.sub("\u2026", "...", text_cleaned_of_u2019_u2018)
        return text_cleaned_of_u2026

    def clear_tags(self, text: str) -> str:
        regex_pattern = r'(<([^>]+)>)'
        return re.sub(regex_pattern, '', text)
