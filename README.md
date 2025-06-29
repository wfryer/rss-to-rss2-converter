# RSS 1.0 to RSS 2.0 Feed Converter

This Python script converts a Pinboard RSS 1.0 (RDF) feed to a valid RSS 2.0 feed for use with tools like [MastoFeed](https://mastofeed.org/) or IFTTT.

## Features

- Converts RSS 1.0 feeds (e.g., from Pinboard) to RSS 2.0
- Saves the output as a `.xml` file on your server
- Compatible with MastoFeed, IFTTT, and other RSS consumers

## Requirements

- SSH access to your web server or VPS
- Python 3.6+
- `feedparser` and `rfeed` Python libraries

## Setup

1. Place `rss_converter.py` on your server (e.g., `/root/rss_converter.py`).
2. Update the `SOURCE_FEED_URL` and `OUTPUT_PATH` in the script with your own values.
3. Run the script manually to generate the feed:

```bash
python3 rss_converter.py
```

4. Confirm the feed is accessible in your browser.

## Automating with Cron

To regenerate the feed every 10 minutes:

```bash
crontab -e
```

Add:

```bash
*/10 * * * * /usr/bin/python3 /root/rss_converter.py
```

## Troubleshooting

- For WordPress sites, adjust `.htaccess` if needed to allow `.xml` files in subdirectories.
- Fix file ownership with:

```bash
chown -R yourcpaneluser:yourcpaneluser /path/to/feed/directory
```

## License

MIT License

## Credits

Developed by Wes Fryer, with assistance from ChatGPT-4o (OpenAI).  
More AI learning resources: [https://ai.wesfryer.com/](https://ai.wesfryer.com/)
