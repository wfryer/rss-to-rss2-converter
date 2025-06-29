#!/usr/bin/env python3
"""
RSS 1.0 (RDF) to RSS 2.0 Feed Converter

Author: Wes Fryer
Collaborator: ChatGPT-4o (OpenAI) — Assisted with development
More AI Learning Resources: https://ai.wesfryer.com/

Purpose:
Converts a Pinboard RSS 1.0 feed to a clean RSS 2.0 feed for use with tools like Mastodon MastoFeed or IFTTT.
"""

import feedparser
from rfeed import *

# URL of your original RSS 1.0 (RDF) feed
# Replace this with your actual feed URL
SOURCE_FEED_URL = "https://your-pinboard-feed-url"

# Location to save the generated RSS 2.0 file
# Replace this with the appropriate path on your server
OUTPUT_PATH = "/path/to/save/your/feed.xml"

d = feedparser.parse(SOURCE_FEED_URL)
items = []

for entry in d.entries:
    item = Item(
        title=entry.title,
        link=entry.link,
        description=entry.get('summary', ''),
    )
    items.append(item)

feed = Feed(
    title="Converted Podcast Recommendations",
    link="https://yourdomain.com/path/to/feed.xml",
    description="RSS 2.0 feed converted from source feed",
    items=items
)

with open(OUTPUT_PATH, "w") as f:
    f.write(feed.rss())

print(f"Feed written to {OUTPUT_PATH}")
