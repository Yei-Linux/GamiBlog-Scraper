blogs_config = [{
    'site_name': 'css-tricks',
    'url': 'https://css-tricks.com/archives/',
    'lua_source': """
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
                """,
    'post': {
        'wrapper': 'article.article-card',
        'title': 'div.article-article h2 a::text',
        'link': 'div.article-article h2 a::attr(href)',
        'src': 'div.article-thumbnail-wrap img::attr(src)',
        'description': 'div.article-article div.card-content p',
    }
}]
