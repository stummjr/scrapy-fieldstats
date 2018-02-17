# -*- coding:utf-8 -*-
import logging
import pprint

from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)


class FieldStatsExtension(object):
    """ When enabled, the FieldStats extension logs the percentage of
        items coverage for a crawl.
    """
    def __init__(self, show_counts=False):
        self.item_count = 0
        self.field_counts = {}
        self.show_counts = show_counts

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('FIELDSTATS_ENABLED'):
            raise NotConfigured

        show_counts = crawler.settings.getbool('FIELDSTATS_COUNTS_ONLY', False)
        ext = cls(show_counts)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def item_scraped(self, item, spider):
        self.compute_item(item)

    def spider_closed(self, spider):
        if self.show_counts:
            report_data = self.field_counts
        else:
            report_data = self.build_fields_summary()

        message = 'Field stats:\n{}'.format(pprint.pformat(report_data))
        logger.info(message)

    def compute_item(self, item):
        self.item_count += 1
        self.count_item_fields(item)

    def count_item_fields(self, item, current_node=None):
        if current_node is None:
            current_node = self.field_counts

        for name, value in item.items():
            if not value:
                continue

            if isinstance(value, dict):
                # recurse into nested items
                if name not in current_node:
                    current_node[name] = {}
                self.count_item_fields(value, current_node=current_node[name])
                continue

            if name not in current_node:
                current_node[name] = 0
            current_node[name] += 1

    def build_fields_summary(self, field_counts=None, fields_summary=None):
        if field_counts is None:
            field_counts = self.field_counts
            fields_summary = {}

        for name, value in field_counts.items():
            if isinstance(value, dict):
                fields_summary[name] = {}
                self.build_fields_summary(field_counts[name], fields_summary[name])
            else:
                field_percentage = int(value) * 100 / self.item_count
                fields_summary[name] = "{}%".format(field_percentage)

        return fields_summary
