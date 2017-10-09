# -*- coding:utf-8 -*-
import logging
import pprint
from collections import defaultdict

from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)


class FieldStatsExtension(object):
    """ When enabled, the FieldStats extensions logs the percentage of
        items coverage for a crawl.
    """
    def __init__(self):
        self.item_count = 0
        self.field_counts = defaultdict(int)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('FIELDSTATS_ENABLED'):
            raise NotConfigured

        ext = cls()
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def item_scraped(self, item, spider):
        self.item_count += 1
        for name, value in item.items():
            if not value:
                continue
            self.field_counts[name] += 1

    def spider_closed(self, spider):
        field_stats = self.compute_fieldstats()
        logger.info('Field stats:\n{}'.format(pprint.pformat(field_stats)))

    def compute_fieldstats(self):
        field_stats = {}
        for name, count in self.field_counts.items():
            field_coverage = int(count) * 100 / self.item_count
            field_stats[name] = "{}%".format(field_coverage)

        return field_stats
