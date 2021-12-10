# Programmableweb Crawler

## 使用

*按顺序执行，在api_data爬完之后再执行api_follower*

#### 爬取API信息
- ```scrapy crawl api_links```
- ```scrapy crawl api_info_links```
- ```scrapy crawl api_data```

#### 爬取API的Followers信息
- ```scrapy crawl api_follower```

#### 爬取Mashup信息
- ```scrapy crawl mashup_links```
- ```scrapy crawl mashup_data```

## 生成数据
- ```data2csv.py``` 将API和Mashup的json数据转换为csv
- ```gen_data.py``` 根据Follower数据生成训练集和测试集

## 数据详情
### 数据为2021年3月29日的数据  
| 名称 | 个数 |
| ----------- | ----------- |
| User | 144583 |
| API | 21030 |
| Mashup | 6437 |
| User-API Interactions | 270701 |

## 声明
此数据来源于[Programmableweb](https://www.programmableweb.com/)  
只用作研究使用，如涉及相关用户信息，请联系删除

