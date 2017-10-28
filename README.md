Scrapy FieldStats
=================

A Scrapy extension that generates a summary of fields coverage from your scraped data.


## What?
Upon finishing a job, Scrapy prints some useful stats about that job, such as: number of requests, responses, scraped items, etc.

However, it's often useful to have an overview of the field coverage in such scraped items. Let's say you want to know the percentage of items missing the `price` field. That's when this extension comes into play!

Check out an example:

```bash
$ scrapy crawl example
2017-10-12 11:10:10 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: examplebot)
...
2017-10-12 11:10:20 [scrapy_fieldstats.fieldstats] INFO: Field stats:
{
    'author': {
        'name': '100.0%',
        'age':  '52.0%'
    },
    'image':  '97.0%',
    'title':  '100.0%',
    'price':  '92.0%',
    'stars':  '47.5%'
}
2017-10-12 11:10:20 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
...
```

## Installation
First, pip install this package:

```bash
$ pip install scrapy-fieldstats
```

## Usage
Enable the extension in your project's `settings.py` file, by adding the following lines:

```python
EXTENSIONS = {
    'scrapy_fieldstats.fieldstats.FieldStatsExtension': 10,
}
FIELDSTATS_ENABLED = True
```
That's all! Now run your job and have a look at the field stats.


## Settings
The settings below can be defined as any other Scrapy settings, as described on [Scrapy docs](https://doc.scrapy.org/en/latest/topics/settings.html#populating-the-settings).

* `FIELDSTATS_ENABLED`: to enable/disable the extension.
* `FIELDSTATS_COUNTS_ONLY`: when `True`, the extension will output absolute counts, instead of percentages.


## Contributing
If you spot a bug, or want to propose a new feature please create an issue in this project's
[issue tracker](https://github.com/stummjr/scrapy-fieldstats/issues).
