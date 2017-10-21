#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy_fieldstats.fieldstats import FieldStatsExtension


def extract_fake_items_and_compute_stats(fake_items, show_counts=False):
    ext = FieldStatsExtension()
    for item in fake_items:
        ext.compute_item(item)

    if show_counts:
        return ext.field_counts
    return ext.build_fields_summary()


def test_single_item():
    fake_items = [{"field1": "value1"}]

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 1
    assert field_stats['field1'] == '100.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 1
    assert field_stats['field1'] == 1


def test_single_item_many_fields():
    fake_items = [
        {
            "field1": "value1",
            "field2": "value2",
        }
    ]

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 2
    assert field_stats['field1'] == '100.0%'
    assert field_stats['field2'] == '100.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 2
    assert field_stats['field1'] == 1
    assert field_stats['field2'] == 1


def test_many_items():
    fake_items = [{"field1": "value1"}, {"field1": "value1"}]

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 1
    assert field_stats['field1'] == '100.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 1
    assert field_stats['field1'] == 2


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

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 2
    assert field_stats['field1'] == '100.0%'
    assert field_stats['field2'] == '100.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 2
    assert field_stats['field1'] == 2
    assert field_stats['field2'] == 2


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

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 2
    assert field_stats['field1'] == '100.0%'
    assert field_stats['field2'] == '50.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 2
    assert field_stats['field1'] == 2
    assert field_stats['field2'] == 1


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

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert len(field_stats) == 2
    assert field_stats['field1'] == '100.0%'
    assert field_stats['field2'] == '50.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert len(field_stats) == 2
    assert field_stats['field1'] == 2
    assert field_stats['field2'] == 1


def test_nested_items():
    fake_items = [
        {
            "field1": "value1",
            "field2": {
                "field2.1": "value2.1",
                "field2.2": "value2.2",
                "field2.3": {
                    "field2.3.1": "value2.3.1",
                    "field2.3.2": "value2.3.2",
                },
            }
        },
        {
            "field1": "value1",
            "field2": {
                "field2.1": "value2.1",
                "field2.3": {
                    "field2.3.1": "value2.3.1",
                    "field2.3.2": "",
                },
                "field2.4": "value2.2",
            }
        }
    ]

    field_stats = extract_fake_items_and_compute_stats(fake_items)
    assert field_stats['field1'] == '100.0%'
    assert field_stats['field2']['field2.1'] == '100.0%'
    assert field_stats['field2']['field2.2'] == '50.0%'
    assert field_stats['field2']['field2.2'] == '50.0%'
    assert field_stats['field2']['field2.3']['field2.3.2'] == '50.0%'

    field_stats = extract_fake_items_and_compute_stats(fake_items, show_counts=True)
    assert field_stats['field1'] == 2
    assert field_stats['field2']['field2.1'] == 2
    assert field_stats['field2']['field2.2'] == 1
    assert field_stats['field2']['field2.2'] == 1
    assert field_stats['field2']['field2.3']['field2.3.2'] == 1
