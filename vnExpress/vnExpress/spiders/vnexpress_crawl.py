import scrapy


class VnexpressCrawlSpider(scrapy.Spider):
    name = 'vnexpress_crawl'
    allowed_domains = ['vnexpress.net']
    start_urls = [
        'https://vnexpress.net/thoi-su',
    ]

    def parse(self, response):
        links_article = response.css('h3.title-news a::attr(href)').getall()
        for link_article in links_article:
            yield scrapy.Request(link_article, callback=self.get)
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def get(self, response):
        title = response.css('h1.title-detail::text').get()
        title = title.strip('? ')
        f = open('D:/PycharmProjects/VnExpress/tutorial/vnExpress/vnExpress/spiders/Output/' + title + '.txt', 'w+',
                 encoding='utf-8')
        f.write('Title: ' + title + '\n')

        category = response.css('ul.breadcrumb li a::text').get()
        f.write('Category: ' + category + '\n')

        update = response.css('span.date::text').get()
        f.write('Update: ' + update + '\n')

        link_article = response.url
        f.write('Link_page: ' + link_article + '\n')

        description = response.css('p.description::text').get()
        f.write('Description: ' + description + '\n'+ 'Content: ' + '\n')

        for i in response.css('article.fck_detail p.Normal'):
            content = ''.join(i.css('*::text').getall())
            f.write(content + '\n')

        image_link = response.css('div.fig-picture img::attr(data-src)').get()
        f.write('Image_link: ' + image_link + '\n')

        image_description = response.css('div.fig-picture img::attr(alt)').get()
        f.write('Image_description: ' + image_description + '\n')

        author = response.css('p.author_mail strong::text').get()
        f.write('Author: ' + author + '\n')

        key_words = response.css('meta[name="keywords"]::attr("content")').get()
        f.write('Keywords: ' + key_words + '\n')

        tags = response.css('meta[name="its_tag"]::attr("content")').get()
        f.write('Tags: ' + tags)


            
''''https://vnexpress.net/goc-nhin',
        'https://vnexpress.net/the-gioi',
        'https://vnexpress.net/kinh-doanh',
        'https://vnexpress.net/giai-tri',
        'https://vnexpress.net/the-thao',
        'https://vnexpress.net/phap-luat',
        'https://vnexpress.net/giao-duc',
        'https://vnexpress.net/suc-khoe',
        'https://vnexpress.net/doi-song',
        'https://vnexpress.net/du-lich',
        'https://vnexpress.net/khoa-hoc',
        'https://vnexpress.net/so-hoa',
        'https://vnexpress.net/oto-xe-may',
        'https://vnexpress.net/y-kien',
        'https://vnexpress.net/tam-su',
        'https://vnexpress.net/hai'''










