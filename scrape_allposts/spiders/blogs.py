import json
from abc import ABC

import scrapy

from scrape_allposts.config.blogs_config import blogs_config
from scrape_allposts.helpers.ParseBlogs import ParseBlogs
from scrapy_splash import SplashRequest, SplashTextResponse
from scrapy.http import HtmlResponse

from scrape_allposts.pojos.Post import Post
from scrape_allposts.pojos.PostItem import PostItem


class BlogsSpider(scrapy.Spider, ParseBlogs, ABC):
    name = 'blogs'

    def start_requests(self):
        for blog in blogs_config:
            url = blog['url']
            lua_source = blog['lua_source']
            post = blog['post']
            site_name = blog['site_name']
            enable = blog['enable']

            if not enable:
                continue

            wrapper = PostItem(text='', selector=post['wrapper'])
            title = PostItem(text='', selector=post['title'])
            link = PostItem(text='', selector=post['link'])
            src = PostItem(text='', selector=post['src'])
            description = PostItem(text='', selector=post['description'])
            post_obj = Post(title=title, link=link, src=src, description=description, wrapper=wrapper)

            yield SplashRequest(url, self.parse, endpoint='execute', args={
                'wait': 5,
                'lua_source': lua_source,
                'timeout': 120,
            }, meta={'post': post_obj, 'site_name': site_name})

    def execute_parse(self, response, post):
        is_only_one_html = isinstance(response, SplashTextResponse)
        pages_response = response if is_only_one_html else response.data
        if not is_only_one_html:
            list_elements = []

            for k, v in pages_response.items():
                response_casted = HtmlResponse(url='scrapied', body=v, encoding='utf-8')
                list_elements = [*self.get_elements(response_casted, post), *list_elements]

            return list_elements
        else:
            response_casted = HtmlResponse(url='scrapied', body=pages_response.body, encoding='utf-8')
            return self.get_elements(response_casted, post)

    def parse(self, response, **kwargs):
        site_name = response.meta['site_name']
        post: Post = response.meta['post']

        elements = self.execute_parse(response, post)

        return {"elements": elements, "site_name": site_name}


