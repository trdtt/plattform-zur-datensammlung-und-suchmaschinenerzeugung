# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import requests


class UrlcrawlerPipeline:
    """
    Collects the RDF-data of the individual crawls and passes them back to the QEnable backend (flask)

    :param all_rdf_data: accumulates all the rdf data collected by the spider
    """

    def open_spider(self, spider):
        """
        This method is called when the spider is created
        :param spider: the spider which scraped the item
        """
        self.all_rdf_data = ''

    def process_item(self, item, spider):
        """
        This method is called for every scraped url & adds the data to the RDF-data collection
        :param item: JSON string containing the rdf data of the last crawled website
        :param spider: the spider which scraped the item
        """
        self.all_rdf_data += item['rdf_data']
        return item

    def close_spider(self, spider):
        """
        This method is called after the completion of the crawling process and sends the data collection to the
        QEnable backend
        :param spider: the spider which scraped the item
        """
        rdf_data_json = {
            'dataset_name': spider.dataset_name,
            'rdf_data': self.all_rdf_data
        }
        requests.post('http://qenable:80/api/upload_triples', json=rdf_data_json)
