from scrape_allposts.pojos.Text import Text
from scrape_allposts.pojos.ValueObject import ValueObject


class PostItem(ValueObject, Text):
    __selector: str

    def __init__(self, text, selector):
        super().__init__()
        self.text = text
        self.__selector = selector

    @property
    def selector(self):
        return self.__selector

    @selector.setter
    def selector(self, selector):
        self.__selector = selector
