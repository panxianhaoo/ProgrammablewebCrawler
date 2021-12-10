import json
import re

pre = "https://www.programmableweb.com"


class SaveAPIlinks:
    @staticmethod
    def process_item(item, spider):
        for i in item['links']:
            write_data('./data/api_links.txt', pre + i)
        return item


class SaveAPIInfoLinks:
    @staticmethod
    def process_item(item, spider):
        item['api_name'] = item['api_name'].replace(' API', '', 1)
        write_data('./data/api_info_links.txt', pre + item['addr'] + '#####' + item['api_name'])
        return item


class SaveAPIData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))

        properties_key.insert(0, 'Desc')
        properties_value.insert(0, process_desc(item['description']))

        properties_key.insert(0, 'Name')
        properties_value.insert(0, item['api_name'])

        properties_key.insert(3, 'Followers')
        properties_value.insert(3, item['followers_num'])

        for i in range(int(item['followers_num']) // 15 + 1):
            write_data('./data/urlwithname.txt',
                       item['url'] + '/followers?pw_view_display_id=list_all&page=' + str(i) + '#####' + item[
                           'api_name'])

        res = dict(zip(properties_key, properties_value))
        write_data('./data/api_data.json', json.dumps(res))
        return item


class SaveFollowerData:
    @staticmethod
    def process_item(item, spider):
        for i in item['followers']:
            write_data('./data/followers_data.txt', i + '#####' + item['api_name'])
        return item


class SaveMashupLinks:
    @staticmethod
    def process_item(item, spider):
        for i in item['links']:
            write_data('./data/mashup_links.txt', pre + i)
        return item


class SaveMashupData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))
        properties_key.insert(0, 'Desc')
        properties_value.insert(0, process_desc(item['description']))

        properties_key.insert(0, 'Name')
        properties_value.insert(0, re.findall(r'<h1>Mashup: (.*?)</h1>', item['mashup_name'])[0])
        res = dict(zip(properties_key, properties_value))
        write_data('./data/mashup_data.json', json.dumps(res))
        return item


class SaveSDKLinks:
    @staticmethod
    def process_item(item, spider):
        for i, j in zip(item['links'], item['related_api_name']):
            write_data('./data/sdk_links.txt', pre + i + '#####' + j)
        return item


class SaveSDKData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        del item['properties_value'][0]
        del item['properties_name'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))

        properties_key.insert(0, 'Related API')
        properties_value.insert(0, item['related_api'])

        properties_key.insert(0, 'Desc')
        properties_value.insert(0, item['description'])

        properties_key.insert(0, 'Name')
        properties_value.insert(0, item['sdk_name'])

        res = dict(zip(properties_key, properties_value))
        write_data('./data/sdk_data.json', json.dumps(res))
        return item


class SaveFrameworkLinks:
    @staticmethod
    def process_item(item, spider):
        for i in item['links']:
            write_data('./data/frameworks_links.txt', pre + i)
        return item


class SaveFrameworkData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))

        properties_key.insert(0, 'Desc')
        properties_value.insert(0, item['description'])

        properties_key.insert(0, 'Name')
        properties_value.insert(0, item['framework_name'])

        res = dict(zip(properties_key, properties_value))
        write_data('./data/framework_data.json', json.dumps(res))
        return item


class SaveLibraryLinks:
    @staticmethod
    def process_item(item, spider):
        for i in item['links']:
            write_data('./data/library_links.txt', pre + i)
        return item


class SaveLibraryData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))

        properties_key.insert(0, 'Desc')
        properties_value.insert(0, item['description'])

        properties_key.insert(0, 'Name')
        properties_value.insert(0, item['library_name'])

        res = dict(zip(properties_key, properties_value))
        write_data('./data/library_data.json', json.dumps(res))
        return item


class SaveSourceLinks:
    @staticmethod
    def process_item(item, spider):
        for i in item['links']:
            write_data('./data/source_links.txt', pre + i)
        return item


class SaveSourceData:
    @staticmethod
    def process_item(item, spider):
        del item['properties_value'][0]
        properties_key = list(map(lambda i: i.lstrip('<label>').split('</label>')[0], item['properties_name']))
        properties_value = list(map(process_value, item['properties_value']))

        properties_key.insert(0, 'Desc')
        properties_value.insert(0, item['description'])

        properties_key.insert(0, 'Name')
        if str(item['source_name']).startswith('Sample Source Code: '):
            item['source_name'] = item['source_name'].split('Sample Source Code: ')[1]
        properties_value.insert(0, item['source_name'])
        res = dict(zip(properties_key, properties_value))
        write_data('./data/source_data.json', json.dumps(res))
        return item


def write_data(file, data):
    w = open(file, 'a+', encoding='utf-8')
    w.write(data + '\n')


def process_value(item):
    item = str(item[6:])
    if not item.startswith('<a'):
        return item.split('</span>')[0]
    else:
        return ",".join(re.findall(r'<a.*?>(.*?)</a>', item))


def process_desc(s):
    s = s.lstrip('<div class=\"api_description tabs-header_description\">')
    if s.startswith('['):
        s = s[s.find(']') + 1:-7]
    else:
        s = s[:-7]
    return s.strip()
