import json
from abc import ABC

import scrapy

from scrape_allposts.helpers.ParseBlogs import ParseBlogs
from scrapy_splash import SplashRequest
from scrapy.http import HtmlResponse

from scrape_allposts.pojos.Post import Post
from scrape_allposts.pojos.PostItem import PostItem


class BlogsSpider(scrapy.Spider, ParseBlogs, ABC):
    name = 'blogs'
    lua_source = """
    function main(splash,args) 
        local htmlsElements = {}
        local numberPageElement
        local nextNumerPageElement
        splash:set_custom_headers({
            ["Accept-Encoding"] = "deflate"
        })
        
        assert(splash:go(args.url))
        
        for i=0,2,1
        do
            if (i ~= 0) 
            then
                numberPageElement = splash:select('.wp_page_numbers ul .active_page')    
                nextNumerPageElement = numberPageElement.node.nextElementSibling
                nextNumerPageElement:mouse_click()            
            end
            assert(splash:wait(10))
            htmlsElements[i] = splash:html()
        end
        
        return htmlsElements
    end
    """

    def start_requests(self):
        urls = ['https://css-tricks.com/archives/']

        for url in urls:
            yield SplashRequest(url, self.parse, endpoint='execute', args={
                'wait': 5,
                'lua_source': self.lua_source,
                'timeout': 120,
            })

    def parse(self, response, **kwargs):
        number = 1
        filename = f'blogs-{number}.json'
        pages_response = response.data

        wrapper = PostItem(text='', selector='article.article-card')
        title = PostItem(text='', selector='div.article-article h2 a::text')
        link = PostItem(text='', selector='div.article-article h2 a::attr(href)')
        src = PostItem(text='', selector='div.article-thumbnail-wrap img::attr(src)')
        description = PostItem(text='', selector='div.article-article div.card-content p')
        post = Post(title=title, link=link, src=src, description=description, wrapper=wrapper)

        list = []

        for k, v in pages_response.items():
            response_casted = HtmlResponse(url='scrapied', body=v, encoding='utf-8')
            list = [*self.get_elements(response_casted, post), *list]

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list, f)

        self.log(f'Saved file as {filename}')
