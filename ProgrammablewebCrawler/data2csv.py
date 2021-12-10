import json

import pandas as pd
from tqdm import tqdm


def api2csv():
    f = open('../data/api_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Desc', 'Primary Category', 'Followers', 'Secondary Categories', 'API Provider', 'API Endpoint',
               'API Portal / Home Page', 'Docs Home Page URL', 'Terms Of Service URL',
               'Supported Request Formats', 'Supported Response Formats',
               'Is This an Unofficial API?', 'Is the API Design/Description Non-Proprietary ?',
               'Restricted Access ( Requires Provider Approval )',
               'Is This a Hypermedia API?', 'SSL Support', 'Architectural Style', 'Twitter URL', 'Authentication Model']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/api.csv', encoding='utf-8')


def mashup2csv():
    f = open('../data/mashup_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Related APIs', 'Categories', 'Desc', 'URL', 'Company', 'Mashup/App Type']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/mashup.csv', encoding='utf-8')


def sdk2csv():
    f = open('../data/sdk_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Desc', 'Related API', 'Related Platform / Languages', 'Categories', 'Added', 'SDK Provider',
               'Asset Home Page (URL)', 'Is the SDK Source Code Non-Proprietary?', 'Device specific',
               'SDK does not belong to a Company', 'Is This an Unofficial SDK ?',
               'Restricted Access ( Requires Provider Approval )']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/sdk.csv', encoding='utf-8')


def framework2csv():
    f = open('../data/framework_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Desc', 'Framework Type', 'Related Platform / Languages', 'Added', 'Framework Provider',
               'Asset Home Page (URL)', 'Repository / Source Code', 'Version',
               'Terms Of Service URL', 'Is the Framework Source Code Non-Proprietary ?',
               'Type of License if Non-Proprietary', 'Device specific', 'Framework does not belong to a Company',
               'Docs Home Page URL', 'Supported Request Formats', 'Supported Response Formats',
               'Offers Hypermedia Support']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/framework.csv', encoding='utf-8')


def library2csv():
    f = open('../data/library_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Desc', 'Library Type', 'Related APIs', 'Related Platform / Languages', 'Categories',
               'Architectural Style', 'Added', 'Library Provider',
               'Asset Home Page (URL)', 'Version',
               'Terms Of Service URL', 'Is the Library Source Code Non-Proprietary ?',
               'Type of License if Non-Proprietary',
               'Type', 'Scope', 'Device specific',
               'Library does not belong to a Company', 'Docs Home Page URL', 'Supported Request Formats',
               'Supported Response Formats', 'Is This an Unofficial Library?', 'Offers Hypermedia Support']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/library.csv', encoding='utf-8')


def source2csv():
    f = open('../data/source_data.json', 'r')
    items = f.readlines()
    columns = ['Name', 'Desc', 'Library Type', 'Related APIs', 'Related Platform / Languages', 'Categories',
               'Added', 'Link to Source Code', 'Sample Source Code Provider']
    df = pd.DataFrame(columns=columns)
    for i in tqdm(items):
        json2dict = json.loads(i)
        df = df.append(json2dict, ignore_index=True)
    df = df.loc[:, columns]
    df.to_csv('../res/source.csv', encoding='utf-8')


mashup2csv()
