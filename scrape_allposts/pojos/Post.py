from scrape_allposts.pojos.PostItem import PostItem


class Post:
    _wrapper: PostItem

    _title: PostItem
    _link: PostItem
    _src: PostItem
    _description: PostItem

    def __init__(self, title, link, src, description, wrapper):
        self._title = title
        self._link = link
        self._src = src
        self._description = description
        self._wrapper = wrapper

    @property
    def wrapper(self):
        return self._wrapper

    @wrapper.setter
    def wrapper(self, wrapper):
        self._wrapper = wrapper

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        self._src = src

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
