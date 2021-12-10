import scrapy


class BasicItem(scrapy.Item):
    def __str__(self):
        return ""


class Links(BasicItem):
    links = scrapy.Field()


class APIInfoLinks(BasicItem):
    addr = scrapy.Field()
    api_name = scrapy.Field()


class APIData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    api_name = scrapy.Field()
    followers_num = scrapy.Field()
    url = scrapy.Field()


class FollowerData(BasicItem):
    followers = scrapy.Field()
    api_name = scrapy.Field()


class MashupData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    mashup_name = scrapy.Field()


class SDKLinks(BasicItem):
    links = scrapy.Field()
    related_api_name = scrapy.Field()


class SDKData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    sdk_name = scrapy.Field()
    related_api = scrapy.Field()


class FrameworkData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    framework_name = scrapy.Field()


class LibraryData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    library_name = scrapy.Field()


class SourceData(BasicItem):
    properties_name = scrapy.Field()
    properties_value = scrapy.Field()
    description = scrapy.Field()
    source_name = scrapy.Field()
