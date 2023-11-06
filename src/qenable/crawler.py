import json
import logging
from urllib.parse import urlparse
from scrapyd_api import ScrapydAPI

crawler_name = 'urlcrawler'
spider_name = 'LinkSpider'


def run_crawler(dataset_name: str, start_urls: [str], allowed_domains: [str] = None, depth_limit: str = '1'):
    """
    Initializes crawling job and sends it to the scrapyd endpoint.
    :param dataset_name: name of the Dataset under which it can be found on QAnswer
    :param start_urls: the URLs from which the spider will begin to crawl
    :param allowed_domains: list of domains that this spider is allowed to crawl
    :param depth_limit: maximum depth that will be crawled
    """
    if allowed_domains is None:
        allowed_domains = []

    logging.info('Initializing Crawler')
    if not allowed_domains:
        for url in start_urls:
            allowed_domains.append(urlparse(url).netloc)

    scrapyd = ScrapydAPI('http://scrapyd:6800')

    scrapyd.schedule(crawler_name, spider_name,
                     settings={
                         'DEPTH_LIMIT': depth_limit
                     },
                     dataset_name=dataset_name,
                     start_urls=json.dumps(start_urls),
                     allowed_domains=json.dumps(allowed_domains),
                     depth_limit=depth_limit
                     )
