import feedparser

def get_news_articles():
    feed = feedparser.parse("https://www.hurriyet.com.tr/rss/gundem.xml")
    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "url": entry.link
        })
    return articles

