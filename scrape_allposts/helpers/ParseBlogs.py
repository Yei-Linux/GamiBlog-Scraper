from typing import List, Dict

from scrape_allposts.pojos.Post import Post


class ParseBlogs:
    def __int__(self):
        pass

    def get_elements(self, response, post: Post) -> List[Dict]:
        list: List[Dict] = []
        cards = response.css(post.wrapper.selector)

        for card in cards:
            title: str = card.css(post.title.selector).get()
            link: str = card.css(post.link.selector).get()
            src: str = card.css(post.src.selector).get()
            description = card.css(post.description.selector).get()

            post.title.text = title
            post.link.text = link
            post.src.text = src
            post.description.text = description

            post.title.clean()
            post.link.clean()
            post.src.clean()
            post.description.clean_tags().clean()

            list.append({"title": post.title.text,
                         "src": post.src.text,
                         "link": post.link.text,
                         "description": post.description.text})

        return list
