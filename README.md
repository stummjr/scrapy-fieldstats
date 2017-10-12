Scrapy FieldStats
=================

A Scrapy extension that generates a summary of fields coverage from your scraped data.


## What?
Upon finishing a job, Scrapy prints some useful stats about that job, such as: number of requests, responses, scraped items, etc.

However, it's often useful to have an overview of the field coverage in such scraped items. Let's say you want to know the percentage of items missing the `price` field. That's when this extension comes into play! Check out an example:


    $ scrapy crawl example
    2017-10-12 11:10:10 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: examplebot)
    ...
    2017-10-12 11:10:20 [scrapy_fieldstats.fieldstats] INFO: Field stats:
    {
        'author': '98.0%',
        'image':  '97.0%',
        'title':  '99.0%',
        'price':  '92.0%',
        'stars':  '47.5%'
    }
    2017-10-12 11:10:20 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    ...


## Installation
First, pip install this package:

    $ pip install scrapy-fieldstats

Then, enable the extension in your project's `setting`.py` file, by adding the following lines:

    EXTENSIONS = {
        'scrapy_fieldstats.fieldstats.FieldStatsExtension': 10,
    }
    FIELDSTATS_ENABLED = True

That's all! Now run your job and have a look at the stats.

## Contributing
If you spot a bug, or want to propose a new feature please create an issue in this project's
[issue tracker](https://github.com/stummjr/scrapy-fieldstats/issues).

## Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
