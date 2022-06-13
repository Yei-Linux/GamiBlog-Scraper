from typing import List, Dict

from scrape_allposts.helpers.CleanerHelper import CleanerHelper


class ParseBlogs(CleanerHelper):
    def __int__(self):
        pass

    def get_elements(self, response) -> List[Dict]:
        list: List[Dict] = []
        cards = response.css("article.article-card")

        for card in cards:
            title: str = card.css("div.article-article h2 a::text").get()
            link: str = card.css("div.article-article h2 a::attr(href)").get()
            src: str = card.css("div.article-thumbnail-wrap img::attr(src)").get()
            description = card.css("div.article-article div.card-content p").get()

            clean_description = self.clean(self.clear_tags(description))

            list.append({"title": self.clean(title), "src": self.clean(src), "link": self.clean(link), "description": clean_description})

        return list
