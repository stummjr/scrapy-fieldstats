#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy_fieldstats.fieldstats import FieldStatsExtension


def fake_extract_items(fake_items, extension):
    for item in fake_items:
        extension.item_scraped(item, None)


def test_single_item():
    fake_items = [{"field1": "value1"}]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 1
    assert field_stats.get('field1') == '100.0%'


def test_single_item_many_fields():
    fake_items = [
        {
            "field1": "value1",
            "field2": "value2",
        }
    ]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 2
    assert field_stats.get('field1') == '100.0%'
    assert field_stats.get('field2') == '100.0%'


def test_many_items():
    fake_items = [{"field1": "value1"}, {"field1": "value1"}]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 1
    assert field_stats.get('field1') == '100.0%'


def test_many_items_many_fields():
    fake_items = [
        {
            "field1": "value1",
            "field2": "value2",
        },
        {
            "field1": "value1",
            "field2": "value2",
        }
    ]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 2
    assert field_stats.get('field1') == '100.0%'
    assert field_stats.get('field2') == '100.0%'


def test_many_items_many_fields_missing_field():
    fake_items = [
        {
            "field1": "value1",
        },
        {
            "field1": "value1",
            "field2": "value2",
        }
    ]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 2
    assert field_stats.get('field1') == '100.0%'
    assert field_stats.get('field2') == '50.0%'


def test_many_items_many_fields_empty_field():
    fake_items = [
        {
            "field1": "value1",
            "field2": "",
        },
        {
            "field1": "value1",
            "field2": "value2",
        }
    ]
    ext = FieldStatsExtension()
    fake_extract_items(fake_items, ext)
    field_stats = ext.compute_fieldstats()
    assert len(field_stats) == 2
    assert field_stats.get('field1') == '100.0%'
    assert field_stats.get('field2') == '50.0%'
