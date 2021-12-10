from ProgrammablewebCrawler.items import *


class GetAPILinks(scrapy.Spider):
    name = 'api_links'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveAPIlinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/apis/directory?page=0&deadpool=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Links()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[2]/table/tbody/tr/td[1]/a/@href').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetAPIInfoLinks(scrapy.Spider):
    name = 'api_info_links'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveAPIInfoLinks': 300
        }
    }

    def start_requests(self):
        f = open('data/api_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = APIInfoLinks()
        item['addr'] = response.xpath('//*[@id="version-details-field"]/div[4]/div[1]/span/a/@href').extract_first()
        item['api_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[1]/div[1]/div[1]/h1/text()').extract_first()
        yield item


class GetAPIData(scrapy.Spider):
    name = 'api_data'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveAPIData': 300
        }
    }

    def start_requests(self):
        f = open('data/api_info_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse,
                                 meta={'apiname': url.split('#####')[1].rstrip(" \n")})

    def parse(self, response, **kwargs):
        item = APIData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/span').extract())
        item['description'] = response.xpath('//*[@id="tabs-header-content"]/div/div[1]').extract_first()
        item['api_name'] = response.meta['apiname']
        item['followers_num'] = \
            response.css('.followers span').extract_first().lstrip('<span> (').split(')</span>')[0]
        item['url'] = response.url
        yield item


class GetFollower(scrapy.Spider):
    name = 'api_follower'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveFollowerData': 300
        }
    }

    def start_requests(self):
        f = open('data/urlwithname.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse,
                                 meta={'apiname': url.split('#####')[1].rstrip(" \n")})

    def parse(self, response, **kwargs):
        item = FollowerData()
        item['followers'] = list(
            response.xpath('//*[@id="followers"]/div[2]/div[2]/table/tbody/tr/td[2]/a/text()').extract())
        item['api_name'] = response.meta['apiname']
        yield item


class GetMashupLinks(scrapy.Spider):
    name = "mashup_links"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveMashupLinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/mashups']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Links()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetMashupData(scrapy.Spider):
    name = "mashup_data"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveMashupData': 300
        }
    }

    def start_requests(self):
        f = open('data/mashup_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse)

    def parse(self, response, **kwargs):
        item = MashupData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div[1]/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div[1]/div/span').extract())
        item['description'] = response.xpath(
            '//*[@id="tabs-header-content"]/div/div[1]/div/div/div/text()').extract_first()
        item['mashup_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1').extract_first()
        yield item


class GetSDKLinks(scrapy.Spider):
    name = "sdk_links"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveSDKLinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/sdk']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = SDKLinks()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        item['related_api_name'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[2]/a/text()').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetSDKData(scrapy.Spider):
    name = 'sdk_data'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveSDKData': 300
        }
    }

    def start_requests(self):
        f = open('data/sdk_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse,
                                 meta={'related_api': url.split('#####')[1].rstrip(" \n")})

    def parse(self, response, **kwargs):
        item = SDKData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div/div/span').extract())
        item['description'] = response.xpath('//*[@id="tabs-header-content"]/div/div[1]/text()').extract_first()
        item['related_api'] = response.meta['related_api']
        item['sdk_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1/text()').extract_first()
        yield item


class GetFrameworkLinks(scrapy.Spider):
    name = "framework_links"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveFrameworkLinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/web-development-frameworks']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Links()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetFrameworkData(scrapy.Spider):
    name = 'framework_data'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveFrameworkData': 300
        }
    }

    def start_requests(self):
        f = open('data/frameworks_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = FrameworkData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div/div/span').extract())
        item['description'] = response.xpath('//*[@id="tabs-header-content"]/div/div[1]/text()').extract_first()
        item['framework_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1/text()').extract_first()
        yield item


class GetLibraryLinks(scrapy.Spider):
    name = "library_links"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveLibraryLinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/api-library']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Links()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetLibraryData(scrapy.Spider):
    name = 'library_data'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveLibraryData': 300
        }
    }

    def start_requests(self):
        f = open('data/library_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = LibraryData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div/div/span').extract())
        item['description'] = response.xpath('//*[@id="tabs-header-content"]/div/div[1]/text()').extract_first()
        item['library_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1/text()').extract_first()
        yield item


class GetSourceLinks(scrapy.Spider):
    name = "source_links"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveSourceLinks': 300
        }
    }

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/sample-source-code']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Links()
        item['links'] = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        yield item
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class GetSourceData(scrapy.Spider):
    name = 'source_data'
    custom_settings = {
        'ITEM_PIPELINES': {
            'ProgrammablewebCrawler.pipelines.SaveSourceData': 300
        }
    }

    def start_requests(self):
        f = open('data/source_links.txt', 'r', encoding='utf-8')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = SourceData()
        item['properties_name'] = list(response.xpath('//*[@id="tabs-content"]/div/div/label').extract())
        item['properties_value'] = list(response.xpath('//*[@id="tabs-content"]/div/div/span').extract())
        item['description'] = response.xpath('//*[@id="tabs-header-content"]/div/div[1]/text()').extract_first()
        item['source_name'] = response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1/text()').extract_first()
        yield item
