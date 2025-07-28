from scraper import get_news_articles
from processor import summarize_article
import json
import os

def main():
    print("🔍 Haberler çekiliyor...")
    articles = get_news_articles()

    summarized = []
    for article in articles:
        print(f"🧠 Özetleniyor: {article['title']}")
        summary = summarize_article(article['title'], article['url'])
        summarized.append({
            "title": article['title'],
            "url": article['url'],
            "summary": summary
        })

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/summary.json", "w", encoding="utf-8") as f:
        json.dump(summarized, f, ensure_ascii=False, indent=2)

    print("✅ İşlem tamamlandı. Özetler 'outputs/summary.json' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()

  