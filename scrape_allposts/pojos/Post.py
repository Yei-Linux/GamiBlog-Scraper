class Post:
    _title: str
    _link: str
    _src: str
    _description: str

    def __int__(self, title, link, src, description):
        self._title = title
        self._link = link
        self._src = src
        self._description = description

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
        return self.description

    @description.setter
    def description(self, description):
        self.description = description
